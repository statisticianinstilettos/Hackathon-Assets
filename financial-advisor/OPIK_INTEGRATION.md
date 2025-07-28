# Financial Advisor with Opik Tracing Integration

This document explains how to use the Financial Advisor agent with **Opik tracing** integration using the official ADK integration approach for monitoring, debugging, and analyzing your AI agent conversations.

## 🎯 What's Been Added

We've integrated [Opik](https://www.comet.com/docs/opik/) tracing into the Financial Advisor agent using the [official ADK integration](https://www.comet.com/docs/opik/tracing/integrations/adk#logging-adk-agent-executions) to provide:

- **📊 Automatic conversation tracking** across the multi-agent workflow
- **🔍 Individual agent performance monitoring** (data analyst, trading analyst, execution analyst, risk analyst)
- **💰 Cost analysis** for each step of the financial advisory process
- **🧵 Session-based threading** to follow the entire user journey
- **📈 Real-time trace visualization** in the Opik dashboard

## 🏗️ Architecture Changes

### Integration Approach

We use the **official ADK integration** with `OpikTracer` and `track_adk_agent_recursive`:

```python
from opik.integrations.adk import OpikTracer, track_adk_agent_recursive

# Create the agent
financial_coordinator = create_financial_coordinator()

# Initialize Opik tracer and apply it to all agents recursively
opik_tracer = OpikTracer()
track_adk_agent_recursive(financial_coordinator, opik_tracer)
```

### What Gets Automatically Tracked

✅ **All agent executions** (main coordinator + 4 sub-agents)  
✅ **Tool usage** (Google Search calls by data analyst)  
✅ **Model interactions** (Gemini API calls and responses)  
✅ **Session continuity** (ADK session ID becomes Opik thread ID)  
✅ **Cost tracking** (Token usage and API costs)  
✅ **Performance metrics** (Response times, success rates)

## 🚀 Getting Started

### 1. Environment Setup

Make sure your `.env` file includes:

```bash
# Gemini API (required)
GOOGLE_GENAI_USE_VERTEXAI=false
GOOGLE_API_KEY=your_gemini_api_key_here

# Opik Configuration (get from https://www.comet.com/)
OPIK_API_KEY=your_actual_opik_api_key
OPIK_WORKSPACE=your_actual_workspace_name
OPIK_PROJECT_NAME=financial-advisor-demo
```

### 2. Install Dependencies

```bash
poetry install  # Opik is already included as a dependency
```

### 3. Run the Demo

```bash
python run_with_opik.py
```

This runs a complete 5-step financial advisory session:
1. **Initial greeting** → Agent introduces itself
2. **Stock analysis** → Data analyst researches AAPL using Google Search
3. **Strategy development** → Trading analyst creates 5 investment strategies
4. **Execution planning** → Execution analyst details implementation
5. **Risk assessment** → Risk analyst evaluates overall plan

## 📊 What You'll See in Opik Dashboard

### Conversation View
- **Thread ID**: ADK session ID for grouping all related traces
- **Complete user journey**: From greeting to final risk assessment
- **Message flow**: User inputs and agent responses for each step

### Agent Graph Tab 🎯 **NEW!**
- **Automatic mermaid graph**: Visual representation of the multi-agent system
- **Complete architecture**: Shows financial coordinator + 4 sub-agents
- **Interactive visualization**: Navigate through the agent relationships
- **Generated automatically** by `track_adk_agent_recursive`

### Agent Traces
Each sub-agent gets its own trace showing:
- **Data Analyst**: Google Search queries and market research
- **Trading Analyst**: Strategy generation and reasoning
- **Execution Analyst**: Implementation planning details
- **Risk Analyst**: Comprehensive risk evaluation

### Performance Metrics
- **Response times** for each agent
- **Token usage** and costs per interaction
- **Success/failure rates** for tool calls
- **Overall conversation completion rates**

## 🔍 Key Features Demonstrated

### Multi-Agent Orchestration
```
Financial Coordinator
├── Data Analyst (Google Search tools)
├── Trading Analyst (Strategy generation)
├── Execution Analyst (Implementation planning)
└── Risk Analyst (Risk evaluation)
```

### Automatic Instrumentation
The `track_adk_agent_recursive` function automatically adds Opik tracing to:
- Main coordinator agent
- All 4 sub-agents
- All tool calls (Google Search)
- All model interactions

### Session Threading
- Uses ADK session ID as Opik thread ID
- Groups entire conversation under one thread
- Enables conversation-level analysis and debugging

## 📈 Real-World Benefits

### 1. **Performance Optimization**
- Identify which agents are slowest (typically data analyst due to Google Search)
- Optimize expensive API calls
- Track cost per successful financial advisory session

### 2. **Quality Assurance**
- Review actual agent responses for accuracy
- Identify when agents provide incorrect financial advice
- Monitor tool usage patterns (search queries, results quality)

### 3. **User Experience Analysis**
- See complete user journey through 5-step process
- Identify where users might get confused
- Track conversation completion rates

### 4. **Cost Management**
- Monitor token usage across all 4 agents
- Track Google Search API usage
- Analyze ROI of different advisory strategies

## 🛠️ Technical Implementation

### ADK Integration Benefits
- **Zero code changes** to agent logic required
- **Automatic instrumentation** of all agents and tools
- **Native session support** for conversation threading
- **Built-in error handling** and trace completion

### Code Structure
```python
# Main agent with integrated tracing
from opik.integrations.adk import OpikTracer, track_adk_agent_recursive

# Simple agent definitions (no Opik code needed)
data_analyst_agent = Agent(...)
trading_analyst_agent = Agent(...)

# One-line integration for entire system
track_adk_agent_recursive(financial_coordinator, opik_tracer)
```

## 🎉 Success Metrics

After running the demo, you should see in your Opik dashboard:

✅ **1 main conversation thread** with complete user journey  
✅ **5+ individual traces** (1 per message exchange + sub-agent calls)  
✅ **Agent graph visualization** in the "Agent graph" tab showing multi-agent structure  
✅ **Google Search tool calls** from the data analyst  
✅ **Cost tracking** for all Gemini API usage  
✅ **Performance data** showing which agents are fastest/slowest  
✅ **Session metadata** including user ID and conversation ID

## 🤝 Support & Documentation

- **Official ADK Integration**: https://www.comet.com/docs/opik/tracing/integrations/adk
- **Opik Documentation**: https://www.comet.com/docs/opik/
- **Multi-Agent Instrumentation**: Uses `track_adk_agent_recursive` experimental feature

## ✨ What Makes This Demo Special

This integration showcases:
- **Real multi-agent workflow** with actual business logic
- **Live tool usage** (Google Search for market data)
- **Complex conversation flow** (5-step structured process)
- **Production-ready patterns** using official ADK integration
- **Complete observability** without code changes to agent logic

Perfect for demonstrating Opik's capabilities with sophisticated AI agent systems! 🚀 