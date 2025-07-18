"""
Example Agentic AI App Hackathon with Google Cloud Run GPUs
Setup Instructions:
-------------------
References:
- Opik Tracing: https://www.comet.com/docs/opik/tracing/log_traces
- ADK integration: https://www.comet.com/docs/opik/tracing/integrations/adk
"""
    
import datetime
from zoneinfo import ZoneInfo

from google.adk.agents import Agent
from opik.integrations.adk import OpikTracer

GOOGLE_API_KEY = "google-api-key"
OPIK_API_KEY = "opik-api-key"
OPIK_PROJECT_NAME = "google-agent-sdk-example"
AGENT_MODEL = "gemini-2.0-flash"
AGENT_NAME = "weather_time_city_agent"


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

