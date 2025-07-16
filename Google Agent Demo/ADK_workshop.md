# Weather Agent Demo with Google ADK + and Opik

A simple demo Weather Agent showcasing the integration of [Google's Agent Development Kit ("ADK")](https://google.github.io/adk-docs/) with [Comet Opik](http://github.com/comet-ml/opik) for observability. 

In this demo you will learn how to demo features:

1. **Build an AI Agents with Google's (ADK)
2. **Use the [Opik ADK integration](https://www.comet.com/docs/opik/tracing/integrations/adk) to log Agent traces

## Setup

1. Install dependencies:
```bash
pip install opik google-adk
```

2. Set up your OpenAI API key:
```bash
# Option A: Create a .env file
OPENAI_API_KEY=your_openai_key_here

# Option B: Export as environment variable
export OPENAI_API_KEY=your_openai_key_here
```

3. Configure Opik:
```bash
opik configure
# Follow prompts for local server address
```

4. Run the demo:
```bash
python ADK_demo.py
```
