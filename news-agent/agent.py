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
    url = f"https://cryptopanic.com/api/v1/posts/"
    
    try:
        params = {
            "auth_token": api_key,
            "kind":"news",
            "filter":"hot"

        }
        response = requests.get(url, params=params)
        
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

                published_at = item.get('published_at', datetime.now().isoformat())

                source = item.get('source', None)
                source_title = "Unknown"
                if source:
                    source_title = source.get('title', 'Unknown')                
                
                news_items.append(NewsData(
                    source=source_title,
                    title=title,
                    summary=title,  # Using title as summary since API doesn't provide summaries
                    sentiment=sentiment,
                    timestamp=published_at
                ))
            
        return news_items
    except requests.exceptions.RequestException as e:
        return f"API Request Error: {str(e)}"

    except json.JSONDecodeError:
        return "API Error: Unable to parse JSON response"

def get_mock_news(limit: int = 5) -> List[NewsData]:
    """Generate mock news data for testing"""
    mock_news = [
        NewsData(
            source="CoinDesk",
            title="Ethereum 2.0 Upgrade Progress: What You Need to Know",
            summary="The Ethereum 2.0 upgrade is progressing well with increasing validator participation.",
            sentiment=0.5,
            timestamp=datetime.now().isoformat()
        )
    ]
    return mock_news[:limit]

async def process_response(ctx: Context, msg: NewsRequest) -> NewsResponse:
    """Process the request and return formatted response"""
    news_items = get_crypto_news(msg.limit)

    for entry in news_items:
        ctx.logger.info(f"Source: {entry.source}")
        ctx.logger.info(f"Title: {entry.title}")
        ctx.logger.info(f"Sentiment: {entry.sentiment}")
    
    return NewsResponse(
        data=news_items,
        status="success",
        timestamp=datetime.now().isoformat()
    )

@agent.on_message(model=NewsRequest)
async def handle_news_request(ctx: Context, sender: str, msg: NewsRequest):
    """Handle incoming request for crypto news"""
    ctx.logger.info(f"Received news request from {sender} for {msg.limit} news items")
    
    #news_items = get_crypto_news(msg.limit)
    response = await process_response(ctx, msg)
    
    await ctx.send(sender, response)

@agent.on_event("startup")
async def startup(ctx: Context):
    """Initialize agent"""
    ctx.logger.info(f"Crypto News Agent started. Address: {agent.address}")
    #dummy_request = NewsRequest(limit=5)
    #await process_response(ctx, dummy_request)

if __name__ == "__main__":
    agent.run()