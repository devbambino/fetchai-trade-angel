from uagents import Agent, Context
from pydantic import BaseModel
from typing import List, Optional
import requests
from datetime import datetime

agent = Agent(name="Crypto Market Data Agent")

# Models
class MarketRequest(BaseModel):
    coin_ids: List[str]

class MarketData(BaseModel):
    name: str
    symbol: str
    current_price: float
    market_cap: float
    total_volume: float
    price_change_24h: float

class MarketResponse(BaseModel):
    data: List[MarketData]
    status: str
    timestamp: str

def get_market_data(coin_ids: List[str]) -> List[MarketData]:
    """Fetch cryptocurrency market data from CoinGecko API"""
    coins_str = ",".join(coin_ids)
    url = f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={coins_str}"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            market_data_list = []
            
            for coin in data:
                market_data_list.append(MarketData(
                    name=coin.get('name', ''),
                    symbol=coin.get('symbol', '').upper(),
                    current_price=coin.get('current_price', 0.0),
                    market_cap=coin.get('market_cap', 0.0),
                    total_volume=coin.get('total_volume', 0.0),
                    price_change_24h=coin.get('price_change_percentage_24h', 0.0)
                ))
            
            return market_data_list
        else:
            # If API fails, return mock data
            raise Exception(f"Failed to get crypto info: {response.text}")
    except Exception as e:
        print(f"Error fetching market data: {e}")
        raise Exception(f"Failed to get crypto info: {e}")

def get_mock_market_data(coin_ids: List[str]) -> List[MarketData]:
    """Generate mock market data for testing"""
    mock_data = {
        "bitcoin": MarketData(
            name="Bitcoin",
            symbol="BTC",
            current_price=50000.0,
            market_cap=950000000000.0,
            total_volume=30000000000.0,
            price_change_24h=2.5
        ),
        "ethereum": MarketData(
            name="Ethereum",
            symbol="ETH",
            current_price=3000.0,
            market_cap=350000000000.0,
            total_volume=15000000000.0,
            price_change_24h=1.8
        ),
        "solana": MarketData(
            name="Solana",
            symbol="SOL",
            current_price=100.0,
            market_cap=35000000000.0,
            total_volume=2000000000.0,
            price_change_24h=-3.2
        )
    }
    
    return [mock_data.get(coin_id, MarketData(
                name=coin_id.capitalize(),
                symbol=coin_id[:3].upper(),
                current_price=100.0,
                market_cap=1000000000.0,
                total_volume=500000000.0,
                price_change_24h=0.0
            )) for coin_id in coin_ids]

async def process_response(ctx: Context, msg: MarketRequest) -> MarketResponse:
    """Process the crypto request and return formatted response"""
    market_data = get_market_data(msg.coin_ids)
    ctx.logger.info(f"Market data: {market_data}")
    return MarketResponse(
        data=market_data,
        status="success",
        timestamp=datetime.now().isoformat()
    )

@agent.on_message(model=MarketRequest)
async def handle_market_request(ctx: Context, sender: str, msg: MarketRequest):
    """Handle incoming request for market data"""
    ctx.logger.info(f"Received market data request from {sender} for coins: {msg.coin_ids}")
    
    #market_data = get_market_data(msg.coin_ids)
    response = await process_response(ctx, msg)
    
    await ctx.send(sender, response)

@agent.on_event("startup")
async def startup(ctx: Context):
    """Initialize agent"""
    ctx.logger.info(f"Crypto Market Data Agent started. Address: {agent.address}")
    #dummy_request = MarketRequest(coin_ids=["bitcoin","ethereum", "solana"])
    #await process_response(ctx, dummy_request)

if __name__ == "__main__":
    agent.run()