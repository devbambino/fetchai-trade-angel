# TradeAngel: AI-Powered Crypto Investment Assistant

![domain:innovation-lab](https://img.shields.io/badge/innovation--lab-3D8BD3)

TradeAngel is an advanced multi-agent AI system built on Fetch.ai's technology stack that helps retail crypto investors make more informed decisions through 24/7 market monitoring, sentiment analysis, and personalized recommendations.

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
3. **Copy .env.example to .env and fill in the appropriate values.**
   ```bash
   cp .env.example .env
   ```
 
4. **Configure your environment variables**:
   ```bash
   ASI1_API_KEY=your_asi_mini_api_key
   CRYPTOPANIC_API_KEY=your_cryptopanic_api_key  # Optional
   ```

## 🏃 Running TradeAngel

The four agents are going to be running already in the Agentverse so you don't need to run them locally. You only need to run the main agent which is the one requesting info from the other four agents regularly in order to make investing recommendations for the coins list provided in the "user_preferences" variable in main.py. The same variable is also useful for adjusting the risk profile(risk_tolerance) of the user, from 1 conservative, to 5 agressive.

1. **(OPTIONAL)Start all agent services in separate terminals(OPTIONAL)**:

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

## 🏆 Hackathon Impact

TradeAngel addresses the critical problem of information overload and emotional trading that plagues retail crypto investors. By leveraging Fetch.ai's agent ecosystem and ASI-1 Mini for intelligent decision-making, the platform democratizes access to sophisticated market analysis previously available only to institutional investors.

Our solution demonstrates the practical applications of the Fetch.ai SDK by creating a network of specialized agents that work in concert through the Agentverse framework to deliver real-world value.

## 👥 Team

- [Dev Bambino] - Architecture & Agent Development, ASI-1 Mini Integration & Data Analysis, API Integration & Technical Documentation

---

*Built with ❤️ using [Fetch.ai](https://fetch.ai)'s SDK and ASI-1 Mini for the Fetch.ai Hackathon.*
