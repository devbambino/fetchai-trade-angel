from uagents import Agent, Context
from pydantic import BaseModel
from typing import List
from datetime import datetime

agent = Agent(name="Crypto Risk Assessment Agent")

# Models
class RiskRequest(BaseModel):
    risk_tolerance: int = 3  # 1-5 scale (1: very conservative, 5: very aggressive)

class RiskAssessment(BaseModel):
    risk_level: int  # 1-5 scale
    factors: List[str]
    timestamp: str

class RiskResponse(BaseModel):
    data: RiskAssessment
    status: str
    timestamp: str

@agent.on_event("startup")
async def startup(ctx: Context):
    """Initialize agent"""
    ctx.logger.info(f"Crypto Risk Assessment Agent started. Address: {agent.address}")

if __name__ == "__main__":
    agent.run()