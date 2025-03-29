import os
from uagents import Agent, Context
from pydantic import BaseModel
from typing import List, Optional
import requests
from datetime import datetime

agent = Agent(name="Crypto News Agent")

# Models
class NewsRequest(BaseModel):
    limit: Optional[int] = 5

class NewsData(BaseModel):
    source: str
    title: str
    summary: str
    sentiment: float  # -1.0 to 1.0
    timestamp: str

class NewsResponse(BaseModel):
    data: List[NewsData]
    status: str
    timestamp: str

def get_crypto_news(limit: int = 5) -> List[NewsData]:
    """Fetch cryptocurrency news from CryptoPanic API"""
    # Get an API key at https://cryptopanic.com/developers/api/
    api_key = os.getenv("CRYPTOPANIC_API_KEY")
    url = f"https://cryptopanic.com/api/v1/posts/?auth_token={api_key}&kind=news&filter=hot"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            news_items = []
            
            for item in data.get('results', [])[:limit]:
                # Simple sentiment analysis (could be replaced with a more sophisticated approach)
                title = item.get('title', '')
                sentiment = 0.0  # Neutral by default
                
                # Very basic sentiment analysis
                positive_words = ['bullish', 'surge', 'gain', 'rise', 'high', 'up', 'positive', 'rally']
                negative_words = ['bearish', 'crash', 'drop', 'fall', 'low', 'down', 'negative', 'plunge']
                
                title_lower = title.lower()
                for word in positive_words:
                    if word in title_lower:
                        sentiment += 0.2
                
                for word in negative_words:
                    if word in title_lower:
                        sentiment -= 0.2
                
                sentiment = max(-1.0, min(1.0, sentiment))  # Clamp to -1.0 to 1.0
                
                news_items.append(NewsData(
                    source=item.get('source', null).get('title', 'Unknown'),
                    title=item.get('title', ''),
                    summary=item.get('title', ''),  # Using title as summary since API doesn't provide summaries
                    sentiment=sentiment,
                    timestamp=item.get('published_at', datetime.now().isoformat())
                ))
            
            return news_items
        else:
            # If API fails, return mock data
            return get_mock_news(limit)
    except Exception as e:
        print(f"Error fetching crypto news: {e}")
        return get_mock_news(limit)

def get_mock_news(limit: int = 5) -> List[NewsData]:
    """Generate mock news data for testing"""
    mock_news = [
        NewsData(
            source="CryptoNews",
            title="Bitcoin Surges Past $50,000 as Institutional Interest Grows",
            summary="Bitcoin has surpassed the $50,000 mark as institutional investors continue to show interest.",
            sentiment=0.8,
            timestamp=datetime.now().isoformat()
        ),
        NewsData(
            source="CoinDesk",
            title="Ethereum 2.0 Upgrade Progress: What You Need to Know",
            summary="The Ethereum 2.0 upgrade is progressing well with increasing validator participation.",
            sentiment=0.5,
            timestamp=datetime.now().isoformat()
        ),
        NewsData(
            source="Blockchain Times",
            title="Solana Experiences Network Downtime, Developers Working on Fix",
            summary="Solana blockchain faced temporary downtime due to network congestion.",
            sentiment=-0.6,
            timestamp=datetime.now().isoformat()
        ),
        NewsData(
            source="Crypto Insider",
            title="Regulatory Concerns Grow as Countries Consider Crypto Restrictions",
            summary="Several countries are introducing stricter regulations for cryptocurrency trading.",
            sentiment=-0.7,
            timestamp=datetime.now().isoformat()
        ),
        NewsData(
            source="DeFi Daily",
            title="New DeFi Protocol Launches with Record TVL",
            summary="A new decentralized finance protocol has launched with over $1B in total value locked.",
            sentiment=0.6,
            timestamp=datetime.now().isoformat()
        )
    ]
    return mock_news[:limit]

@agent.on_message(model=NewsRequest)
async def handle_news_request(ctx: Context, sender: str, msg: NewsRequest):
    """Handle incoming request for crypto news"""
    ctx.logger.info(f"Received news request from {sender} for {msg.limit} news items")
    
    news_items = get_crypto_news(msg.limit)
    
    response = NewsResponse(
        data=news_items,
        status="success",
        timestamp=datetime.now().isoformat()
    )
    
    await ctx.send(sender, response)

@agent.on_event("startup")
async def startup(ctx: Context):
    """Initialize agent"""
    ctx.logger.info(f"Crypto News Agent started. Address: {agent.address}")

if __name__ == "__main__":
    agent.run()