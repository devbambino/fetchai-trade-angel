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

def assess_risk(risk_tolerance: int) -> RiskAssessment:
    """Generate a risk assessment based on user risk tolerance and market conditions"""
    # This would typically use real market data, fear greed index, etc.
    # Here we're keeping it simple for the example
    
    # Risk level is influenced by user's risk tolerance, but can be adjusted based on market conditions
    risk_level = risk_tolerance
    
    # Generate risk factors based on risk level
    factors = []
    
    if risk_level <= 2:  # Conservative
        factors = [
            "Current market volatility suggests caution",
            "Focus on established cryptocurrencies (BTC, ETH)",
            "Consider stablecoin allocation for security",
            "Limit exposure to altcoins"
        ]
    elif risk_level == 3:  # Moderate
        factors = [
            "Balanced approach recommended in current market",
            "Mix of established coins and select altcoins",
            "Consider DeFi opportunities with proper research",
            "Maintain emergency liquidity"
        ]
    else:  # Aggressive
        factors = [
            "Higher risk tolerance allows for emerging coin opportunities",
            "Consider timing market cycles for entry/exit",
            "Research fundamentals of newer projects",
            "Set stop-loss levels for speculative positions"
        ]
    
    return RiskAssessment(
        risk_level=risk_level,
        factors=factors,
        timestamp=datetime.now().isoformat()
    )

async def process_response(ctx: Context, msg: RiskRequest) -> RiskResponse:
    """Process the request and return formatted response"""
    risk_assessment = assess_risk(msg.risk_tolerance)

    ctx.logger.info(f"risk_level: {risk_assessment.risk_level}")
    ctx.logger.info(f"factors: {risk_assessment.factors}")
    ctx.logger.info(f"timestamp: {risk_assessment.timestamp}")
        
    return RiskResponse(
        data=risk_assessment,
        status="success",
        timestamp=datetime.now().isoformat()
    )

@agent.on_message(model=RiskRequest)
async def handle_risk_request(ctx: Context, sender: str, msg: RiskRequest):
    """Handle incoming request for risk assessment"""
    ctx.logger.info(f"Received risk assessment request from {sender} with risk tolerance: {msg.risk_tolerance}")
    
    #risk_assessment = assess_risk(msg.risk_tolerance)
    response = await process_response(ctx, msg)
    
    await ctx.send(sender, response)

@agent.on_event("startup")
async def startup(ctx: Context):
    """Initialize agent"""
    ctx.logger.info(f"Crypto Risk Assessment Agent started. Address: {agent.address}")
    #dummy_request = RiskRequest(risk_tolerance=5)
    #await process_response(ctx, dummy_request)

if __name__ == "__main__":
    agent.run()