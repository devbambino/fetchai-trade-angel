# Fear and Greed Index Agent 📊

![domain:innovation-lab](https://img.shields.io/badge/innovation--lab-3D8BD3)

## Description

This AI Agent fetches and processes the Fetch Fear & Greed Index from Alternative.me API, providing insights into market sentiment. The Fear and Greed Index is a valuable tool for understanding market psychology and potential trend changes in the cryptocurrency market.

## Features

- Fetches real-time Fear and Greed Index data
- Provides classification of market sentiment
- Returns structured data using Pydantic models
- Includes timestamp information for the data point

## Input Data Model

```python
class FearGreedRequest(BaseModel):
    limit: Optional[int] = 1 # Limit the number of returned results
```

## Output Data Models

```python
class FearGreedData(BaseModel):
    value: float
    value_classification: str
    timestamp: str

class FearGreedResponse(BaseModel):
    data: List[FearGreedData]
    status: str
    timestamp: str
```