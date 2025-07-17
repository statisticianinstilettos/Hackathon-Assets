# Weather Agent Demo with Google ADK + and Opik

A simple demo Weather Agent showcasing the integration of [Google's Agent Development Kit ("ADK")](https://google.github.io/adk-docs/) with [Comet Opik](http://github.com/comet-ml/opik) for observability. 

In this demo you will learn how to demo features:

1. **Build an AI Agents with Google's (ADK)
2. **Use the [Opik ADK integration](https://www.comet.com/docs/opik/tracing/integrations/adk) to log Agent traces.

To track your ADK agent’s activity, use OpikTracer. This tracker records everything your agent does and saves it to Opik.

## Setup

🚀 To run this demo: (for MAC obviously)
1. Clone this repo: git clone https://github.com/statisticianinstilettos/Hackathon-Assets.gi
2. Open your terminal and navigate to the project directory: cd path/to/your/project
3. Create a virtual environment: python3 -m venv venv
4. Activate the virtual environment: source venv/bin/activate
5. Install the Requirements in your virtual environment: python3 -m pip install opik google-adk 
6. Configure your API keys
   - Create a .env file: touch .env
   - open it: nano .env
   - Add your API keys to the file. Paste in:
        GOOGLE_API_KEY = your_google_key_here
        OPIK_API_KEY = your_opik_key_here
        OPIK_PROJECT_NAME = "google-agent-sdk-example"
   - Press Ctrl + O to save, Enter to confirm.
   - Press Ctrl + X to exit.
8. Run the app locally: python3 ADK_demo.py
9. Check for your traces in Opik under the project name  "google-agent-sdk-example"

1. Install dependencies:
```bash
pip install opik google-adk 
```

2. Set up your Google API key:
```bash
# Option A: Create a .env file
GOOGLE_API_KEY=your_google_key_here

# Option B: Export as environment variable
export GOOGLE_API_KEY=your_google_key_here
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

5. Check out your traces in the Opik UI!
![Example Trace](https://i.imgur.com/41Ts9Qll.png)

## Project Structure

- `recipe_agent.py`: Main application file containing agent definitions and logic
- `.env`: (Optional) Environment variables file for API keys
