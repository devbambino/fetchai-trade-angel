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

@agent.on_event("startup")
async def introduce_agent(ctx: Context):
    """Introduces the TradeAngel agent"""
    ctx.logger.info(f"Hello! I'm {agent.name} and my address is {agent.address}.")
    print(f"Hello! I'm {agent.name} and my address is {agent.address}.")

@agent.on_interval(period=4 * 60 * 60.0)  # Every 4 hours
async def request_market_data(ctx: Context):
    """Request market data for monitored assets"""
    await ctx.send(MARKET_DATA_AGENT, MarketDataRequest(
        coins=["bitcoin", "ethereum", "solana"]
    ))
    
    await ctx.send(NEWS_AGENT, NewsRequest(
        topics=["crypto markets", "bitcoin price", "ethereum price", "u.s. stocks markets"]
    ))

# Message handlers and AI integration


# Run the agent
if __name__ == "__main__":
    agent.run()