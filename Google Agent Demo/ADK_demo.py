"""
Example Agentic AI App Hackathon with Google Cloud Run GPUs
Setup Instructions:
-------------------
1. Install dependencies:
    pip install openai-agents opik python-dotenv
2. Set up all your API keys:
   Option A) Create a .env file in the project root:
    OPIK_API_KEY=your_opik_key_here
   Option B) Export as environment variable:
    export OPIK_API_KEY=your_opik_key_here
3. Configure Opik (for tracing and online evals):
    opik configure
   # Follow prompts for local server address
4. Run the script:
    python ADK_demo.py
References:
- Opik Tracing: https://www.comet.com/docs/opik/tracing/log_traces
- ADK integration: https://www.comet.com/docs/opik/tracing/integrations/adk
"""
    
import os
import datetime
from zoneinfo import ZoneInfo
from dotenv import load_dotenv

from google.adk.agents import Agent
from google.adk.runners import Runner
from opik.integrations.adk import OpikTracer

AGENT_MODEL = "gemini-2.0-flash"
AGENT_NAME = "weather_time_city_agent"

# Load environment variables from .env file
load_dotenv()

# Verify OpenAI API key is set
if not os.getenv("GOOGLE_API_KEY"):
    raise ValueError("GOOGLE_API_KEY environment variable is not set")
if not os.getenv("OPIK_API_KEY"):
    raise ValueError("OPIK_API_KEY environment variable is not set")

def get_weather(city: str) -> dict:
    if city.lower() == "new york":
        return {
            "status": "success",
            "report": (
                "The weather in New York is sunny with a temperature of 25 degrees"
                " Celsius (41 degrees Fahrenheit)."
            ),
        }
    else:
        return {
            "status": "error",
            "error_message": f"Weather information for '{city}' is not available.",
        }


def get_current_time(city: str) -> dict:
    if city.lower() == "new york":
        tz_identifier = "America/New_York"
    else:
        return {
            "status": "error",
            "error_message": (f"Sorry, I don't have timezone information for {city}."),
        }

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = f'The current time in {city} is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
    return {"status": "success", "report": report}

#To track your ADK agent’s activity, use OpikTracer. This tracker records everything your agent does and saves it to Opik:
opik_tracer = OpikTracer()

root_agent = Agent(
    name="weather_time_agent",
    model="gemini-2.0-flash-exp",
    description=("Agent to answer questions about the time and weather in a city."),
    instruction=("I can answer your questions about the time and weather in a city."),
    tools=[get_weather, get_current_time],
    before_agent_callback=opik_tracer.before_agent_callback,
    after_agent_callback=opik_tracer.after_agent_callback,
    before_model_callback=opik_tracer.before_model_callback,
    after_model_callback=opik_tracer.after_model_callback,
    before_tool_callback=opik_tracer.before_tool_callback,
    after_tool_callback=opik_tracer.after_tool_callback,
)

from google.adk.runners import Runner

if __name__ == "__main__":
    city = input("Enter a city: ")

    runner = Runner(
        agent=root_agent,
        app_name="weather_time_app",
        session_service=None  # Optional, will default to in-memory if not provided
    )

    result = runner.run({"input": city})
    print(result.text)
