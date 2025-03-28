from uagents import Agent, Context, Model
from typing import Optional
from asi.llm import query_llm

# Initialize the TradeAngel agent
agent = Agent(name="TradeAngel Assistant", mailbox=True, port=8001)

# Hosted agent addresses (Agentverse addresses)
NEWS_AGENT = "agent1qxxxxxxxxxxxxxxxxxxxxxxxxxx"
MARKET_DATA_AGENT = "agent1qyyyyyyyyyyyyyyyyyyyyyy"
RISK_AGENT = "agent1qzzzzzzzzzzzzzzzzzzzzzzzz"

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

class InvestmentRecommendation(Model):
    action: str  # BUY, SELL, HOLD
    confidence: float
    reasoning: str
    coins: list[dict]

@agent.on_event("startup")
async def introduce_agent(ctx: Context):
    """Introduce the CryptoSage agent"""
    ctx.logger.info(f"CryptoSage assistant initialized with address {agent.address}")

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