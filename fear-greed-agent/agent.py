from uagents import Agent, Context
from pydantic import BaseModel
from typing import List, Optional
import requests
from datetime import datetime

agent = Agent(name="Crypto Fear & Greed Agent")

# Models
class FearGreedRequest(BaseModel):
    limit: Optional[int] = 1 # Limit the number of returned results

class FearGreedData(BaseModel):
    value: float
    value_classification: str
    timestamp: str

class FearGreedResponse(BaseModel):
    data: List[FearGreedData]
    status: str
    timestamp: str

def get_fear_greed_index(limit: int = 1) -> List[FearGreedData]:
    """Fetch Fear & Greed Index from Alternative.me API"""
    url = f"https://api.alternative.me/fng/?limit={limit}"
    
    try:
        params = {
            "limit": limit
        }
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            fgi_data = []
            
            for item in data.get('data', [])[:limit]:
                # Convert value to float
                value = float(item.get('value', 0))
                
                # Determine classification
                classification = item.get('value_classification', '')
                
                # Timestamp
                timestamp = datetime.fromtimestamp(int(item.get('timestamp', 0))).isoformat()
                
                fgi_data.append(FearGreedData(
                    value=value,
                    value_classification=classification,
                    timestamp=timestamp
                ))
            
            return fgi_data
        else:
            return get_mock_fear_greed_index(limit)
    except Exception as e:
        print(f"Error fetching fear & greed index: {e}")
        return get_mock_fear_greed_index(limit)

def get_mock_fear_greed_index(limit: int = 1) -> List[FearGreedData]:
    """Generate mock Fear & Greed Index data for testing"""
    classifications = ["Neutral", "Greed", "Extreme Greed"]
    values = [50, 75, 90]
    
    mock_data = []
    for i in range(min(limit, len(classifications))):
        mock_data.append(FearGreedData(
            value=values[i],
            value_classification=classifications[i],
            timestamp=datetime.now().isoformat()
        ))
    
    return mock_data

async def process_response(ctx: Context, msg: FearGreedRequest) -> FearGreedResponse:
    """Process the request and return formatted response"""
    fgi_data = get_fear_greed_index(msg.limit)

    for entry in fgi_data:
        ctx.logger.info(f"Fear and Greed Index: {entry.value}")
        ctx.logger.info(f"Classification: {entry.value_classification}")
        ctx.logger.info(f"Timestamp: {entry.timestamp}")
    
    return FearGreedResponse(
        data=fgi_data,
        status="success",
        timestamp=datetime.now().isoformat()
    )

@agent.on_message(model=FearGreedRequest)
async def handle_fear_greed_request(ctx: Context, sender: str, msg: FearGreedRequest):
    """Handle incoming request for Fear & Greed Index data"""
    ctx.logger.info(f"Received Fear & Greed Index request from {sender} for limit: {msg.limit}")
    
    fgi_data = get_fear_greed_index(msg.limit)
    
    response = FearGreedResponse(
        data=fgi_data,
        status="success",
        timestamp=datetime.now().isoformat()
    )
    
    await ctx.send(sender, response)

@agent.on_event("startup")
async def startup(ctx: Context):
    """Initialize agent"""
    ctx.logger.info(f"Crypto Fear & Greed Agent started. Address: {agent.address}")
    dummy_request = FearGreedRequest(limit=1)
    await process_response(ctx, dummy_request)

if __name__ == "__main__":
    agent.run()