from uagents import Agent, Bureau, Context, Model, Protocol
from uagents.setup import fund_agent_if_low
from typing import List, Dict, Optional
from asi.llm import query_asi
from pydantic import Field
import asyncio
from datetime import datetime, timedelta
import json

# Import Agentverse SDK components
from uagents.network import get_agentverse_client

# Data models
class MarketDataRequest(Model):
    coins: list[str]
    timeframe: str = "24h"

class MarketDataResponse(Model):
    data: dict
    timestamp: str

class NewsRequest(Model):
    topics: list[str]
    limit: int = 5

class NewsResponse(Model):
    articles: list
    sentiment_score: float
    timestamp: str

class NewsData(Model):
    source: str
    title: str
    summary: str
    sentiment: float = Field(default=0.0)  # -1.0 to 1.0
    timestamp: str

class MarketData(Model):
    symbol: str
    price: float
    change_24h: float
    volume_24h: float
    market_cap: float
    timestamp: str

class FearGreedIndex(Model):
    value: int  # 0-100
    classification: str
    timestamp: str

class RiskAssessment(Model):
    risk_level: str  # Low, Medium, High
    factors: List[str]
    timestamp: str

class CryptoRecommendation(Model):
    coin: str
    action: str  # BUY, SELL, HOLD
    confidence: float  # 0.0 to 1.0
    reasoning: str
    timestamp: str

@agent.on_event("startup")
async def introduce_agent(ctx: Context):
    """Introduces the TradeAngel agent"""
    ctx.logger.info(f"TradeAngel assistant initialized with address {agent.address}")
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


# Define agent addresses for Agentverse hosted agents
NEWS_AGENT_ADDRESS = "agent1qvldq34su4py9y5d9rqrcwl07ah0h6825dhhlamzkzpl3dvkq9w4uhz02px" # To be replaced with actual address
MARKET_DATA_AGENT_ADDRESS = "agent1q23w0r6t9j8aneev4gg02k2kp72yqfnphqsjddxn2kwj754ysn42kkl0g9d" # To be replaced with actual address
RISK_AGENT_ADDRESS = "agent1qv43f94u8r43xqdn0dgg27n7zfxe0tekx8d00c0hrsug69dz47swwagcgwh" # To be replaced with actual address
FEAR_GREED_AGENT_ADDRESS = "agent1qfff9tcxq2xn6n3664f2jpqmgza0lpnlz33m9prcj9f0a4kn0yzpsfa6yuz" # To be replaced with actual address

# Initialize the TradeAngel main agent
agent = Agent(
    name="TradeAngel Assistant",
    port=8000,
    seed="project_seed_phrase",
    endpoint=["http://localhost:8000/submit"],
)

fund_agent_if_low(agent.wallet.address())

# Initialize storage for collected data
agent_storage = {
    "news_data": [],
    "market_data": null,
    "fear_greed_index": None,
    "risk_assessment": None,
    "user_preferences": {
        "risk_tolerance": "medium",  # low, medium, high
        "investment_horizon": "medium",  # short, medium, long
        "coins_of_interest": ["BTC", "ETH", "SOL"]
    }
}

# Message handlers and AI integration

# On startup
@agent.on_event("startup")
async def on_startup(ctx: Context):
    ctx.logger.info("TradeAngel starting up...")

# Run the agent
if __name__ == "__main__":
    agent.run()