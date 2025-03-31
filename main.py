from uagents import Agent, Context, Bureau
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from asi.llm import query_llm

# Initialize the TradeAngel main agent
agent = Agent(name="TradeAngel Agent", mailbox=True, port = 8001)

# Define agent addresses for Agentverse hosted agents
NEWS_AGENT_ADDRESS = "agent1qvldq34su4py9y5d9rqrcwl07ah0h6825dhhlamzkzpl3dvkq9w4uhz02px" # To be replaced with actual address
MARKET_DATA_AGENT_ADDRESS = "agent1q23w0r6t9j8aneev4gg02k2kp72yqfnphqsjddxn2kwj754ysn42kkl0g9d" # To be replaced with actual address
RISK_AGENT_ADDRESS = "agent1qv43f94u8r43xqdn0dgg27n7zfxe0tekx8d00c0hrsug69dz47swwagcgwh" # To be replaced with actual address
FEAR_GREED_AGENT_ADDRESS = "agent1qfff9tcxq2xn6n3664f2jpqmgza0lpnlz33m9prcj9f0a4kn0yzpsfa6yuz" # To be replaced with actual address

# Coins to monitor
COINS = ["bitcoin", "ethereum", "solana"]

# Data models
class NewsRequest(BaseModel):
    limit: Optional[int] = 5

class MarketRequest(BaseModel):
    coin_ids: List[str]

class FearGreedRequest(BaseModel):
    limit: Optional[int] = 1

class RiskRequest(BaseModel):
    risk_tolerance: int = 3  # 1-5 scale (1: very conservative, 5: very aggressive)

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

class FearGreedData(BaseModel):
    value: float
    value_classification: str
    timestamp: str

class FearGreedResponse(BaseModel):
    data: List[FearGreedData]
    status: str
    timestamp: str

class RiskAssessment(BaseModel):
    risk_level: int  # 1-5 scale
    factors: List[str]
    timestamp: str

class RiskResponse(BaseModel):
    data: RiskAssessment
    status: str
    timestamp: str

class CryptoRecommendation(BaseModel):
    coin: str
    action: str  # BUY, SELL, HOLD
    confidence: float  # 0.0 to 1.0
    reasoning: str
    timestamp: str

# Global variables to store agent responses
news_data = None
market_data = None
fear_greed_data = None
risk_assessment = None
user_preferences = {
    "risk_tolerance": 3,  # Default medium risk tolerance
    "favorite_coins": ["bitcoin", "ethereum", "solana"]
}

# Message handlers and AI integration
@agent.on_event("startup")
async def introduce_agent(ctx: Context):
    """Introduces the TradeAngel agent"""
    ctx.logger.info(f"Hello! I'm {agent.name} and my address is {agent.address}.")
    print(f"Hello! I'm {agent.name} and my address is {agent.address}.")
    await request_all_data(ctx)

@agent.on_interval(period=2 * 60.0)  # Runs every 2 minutes
async def request_all_data(ctx: Context):
    """Requests data from all agents every 2 minutes."""
    try:
        await ctx.send(NEWS_AGENT, NewsRequest())
        await ctx.send(MARKET_DATA_AGENT, MarketRequest(coin_ids=COINS))
        await ctx.send(FEAR_GREED_AGENT, FearGreedRequest())
        await ctx.send(RISK_AGENT, RiskRequest(risk_tolerance=user_preferences["risk_tolerance"]))
    except Exception as e:
        ctx.logger.error(f"Error requesting data: {e}")

@agent.on_message(model=NewsResponse)
async def handle_news_response(ctx: Context, sender: str, msg: NewsResponse):
    """Handles incoming news data."""
    global news_data
    news_data = msg
    ctx.logger.info(f"Received news data from {sender}")
    ctx.logger.info(f"Received news data:{msg}")
    await generate_recommendation_if_ready(ctx)

@agent.on_message(model=MarketResponse)
async def handle_market_response(ctx: Context, sender: str, msg: MarketResponse):
    """Handles incoming market data."""
    global market_data
    market_data = msg
    ctx.logger.info(f"Received market data from {sender}")
    ctx.logger.info(f"Received market data:{msg}")
    await generate_recommendation_if_ready(ctx)

@agent.on_message(model=FearGreedResponse)
async def handle_fear_greed_response(ctx: Context, sender: str, msg: FearGreedResponse):
    """Handles incoming fear and greed index data."""
    global fear_greed_data
    fear_greed_data = msg
    ctx.logger.info(f"Received fear and greed data from {sender}")
    ctx.logger.info(f"Received fear and greed data:{msg}")
    await generate_recommendation_if_ready(ctx)

@agent.on_message(model=RiskResponse)
async def handle_risk_response(ctx: Context, sender: str, msg: RiskResponse):
    """Handles incoming risk assessment."""
    global risk_assessment
    risk_assessment = msg
    ctx.logger.info(f"Received risk assessment from {sender}")
    ctx.logger.info(f"Received risk assessment:{msg}")
    await generate_recommendation_if_ready(ctx)

async def generate_recommendation_if_ready(ctx: Context):
    """Generates investment recommendations if all required data is available."""
    global news_data, market_data, fear_greed_data, risk_assessment
    
# Run the agent
if __name__ == "__main__":
    agent.run()