# TradeAngel: AI-Powered Crypto Investment Assistant

![domain:innovation-lab](https://img.shields.io/badge/innovation--lab-3D8BD3)

TradeAngel is an advanced multi-agent AI system built on Fetch.ai's technology stack that helps retail crypto investors make more informed decisions through 24/7 market monitoring, sentiment analysis, and personalized recommendations.

## 🏆 Impact and Inspiration

TradeAngel addresses the critical problem of information overload and emotional trading that plagues retail crypto investors. By leveraging Fetch.ai's agent ecosystem and ASI-1 Mini for intelligent decision-making, the platform democratizes access to sophisticated market analysis previously available only to institutional investors.

Our solution demonstrates the practical applications of the Fetch.ai SDK by creating a network of specialized agents that work in concert through the Agentverse framework to deliver real-world value.

This project was inspired on DevBambino's personal experience with retail investing, who tired of losing money in the crypto markets decided to create his own manual process(collecting and analazying crypto and stocks markets news, fear indexes, and price data) to make informed investing decisions. That manual process was the reference for Trade Angel automated analysis.

## 🌟 Features

- **Multi-Agent Intelligence Network**:
  - 📰 **News Sentiment Agent**: Monitors crypto news sources and performs sentiment analysis
  - 📊 **Market Data Agent**: Tracks real-time prices, volumes, and market trends
  - 😱 **Fear & Greed Agent**: Analyzes market sentiment using the Fear & Greed Index
  - ⚖️ **Risk Assessment Agent**: Evaluates investment risk based on multiple factors
  - 🧠 **TradeAngel Assistant**: Processes all agent data to generate actionable recommendations

- **Advanced Analysis**:
  - Sentiment analysis of news using NLP
  - Technical market indicators tracking
  - Risk assessment calibrated to user preferences
  - Decision support powered by ASI-1 Mini LLM

- **User Benefits**:
  - 24/7 market monitoring without emotional bias
  - Information consolidation from multiple sources
  - Clear BUY/SELL/WAIT recommendations with confidence scores
  - Educational insights explaining recommendation reasoning

## 🛠️ Tech Stack

- **[Fetch.ai](https://fetch.ai) Framework**:
  - uAgents for autonomous agent development
  - ASI-1 Mini LLM for context processing and decision making
  
- **APIs**:
  - CryptoPanic (news aggregation)
  - CoinGecko (market data)
  - Alternative.me (Fear & Greed Index)

- **Libraries**:
  - Python with asyncio for asynchronous operations
  - Requests for API interactions
  - dotenv for environment variable management

## 📋 Prerequisites

- Python 3.10+
- Fetch.ai SDK & ASI-1 Mini access
- API keys for CryptoPanic, CoinGecko (optional)
- Git (for cloning the repository)

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/devbambino/fetchai-trade-angel.git
   cd fetchai-trade-angel
   ```

2. **Install dependencies**:
   ```bash
   pip install uagents asi-one requests python-dotenv
   ```

3. **Create an environment file**:
   ```bash
   # Create .env file with the following variables
   ASI1_API_KEY=your_asi_mini_api_key
   CRYPTOPANIC_API_KEY=your_cryptopanic_api_key  
   ```

## 🏃 Running TradeAngel

1. **Start all agent services in separate terminals**:

   ```bash
   # Terminal 1: News Agent
   python news-agent/agent.py
   
   # Terminal 2: Market Data Agent
   python market-data-agent/agent.py
   
   # Terminal 3: Fear & Greed Agent
   python fear-greed-agent/agent.py
   
   # Terminal 4: Risk Agent
   python risk-agent/agent.py
   ```

2. **Launch the TradeAngel Assistant**:
   ```bash
   # Terminal 5: Main TradeAngel Agent
   python main.py
   ```

3. **Interact with recommendations**:
   TradeAngel will start collecting data from all agents, analyze it using ASI-1 Mini LLM, and print investment recommendations to the console.

## 📁 Project Structure

```
TradeAngel/
├── .env                      # Environment variables
├── main.py                   # TradeAngel main assistant agent
├── asi/
│   └── llm.py                # ASI-1 Mini integration
├── fear-greed-agent/
│   ├── agent.py              # Fear & Greed Index agent
│   └── readme.md   
├── market-data-agent/
│   ├── agent.py              # Cryptocurrency market data agent
│   └── readme.md   
├── news-agent/
│   ├── agent.py              # News sentiment analysis agent
│   └── readme.md    
├── risk-agent/
│   ├── agent.py              # Risk assessment agent
│   └── readme.md        
└── README.md
```

## 🛣️ How It Works

1. **Data Collection**: Each specialized agent monitors a specific data source (news, market data, sentiment indices)
2. **Communication**: Agents respond to periodic requests from the main TradeAngel agent
3. **Analysis**: The TradeAngel agent aggregates data from all sources
4. **AI Decision Making**: ASI-1 Mini processes the consolidated data to generate recommendations
5. **Recommendation Delivery**: TradeAngel presents actionable insights with confidence levels and reasoning

## 🔮 Future Enhancements

- **Web Interface**: User dashboard for monitoring recommendations and portfolio performance
- **Additional Agents**: On-chain analytics, regulatory monitoring, technical analysis
- **Portfolio Management**: Automatic portfolio tracking and rebalancing suggestions
- **Backtesting Module**: Test strategies against historical data
- **User Feedback Loop**: Learning from user actions to improve recommendations
- **Mobile Alerts**: Push notifications for critical market events
- **Advanced Multi-chain Support**: Beyond major cryptocurrencies to emerging protocols

## 👥 Team

- [Dev Bambino] - Architecture & Agent Development, ASI-1 Mini Integration & Data Analysis, API Integration & Technical Documentation

## ❤️ Acknowledgements and Thanks

The resources and workshops offered by the Fecth.ai team were super helpful. We also found the documentation in fetch.ai website easy to understand and easy to implement. Thanks to them we were able to complete our project in less than a week.

---

*Built with ❤️ using [Fetch.ai](https://fetch.ai)'s SDK and ASI-1 Mini for the Fetch.ai Hackathon.*
