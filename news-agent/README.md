# Crypto news Agent 📊

![domain:innovation-lab](https://img.shields.io/badge/innovation--lab-3D8BD3)

## Description

This AI Agent fetches and processes crypto news from CryptoPanic API

## Features

- Item

## Input Data Model

```python
class NewsRequest(BaseModel):
    limit: Optional[int] = 5
```

## Output Data Models

```python
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
```