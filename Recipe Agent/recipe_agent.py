"""
Sample Recipe Agent Demo for OpenAI Hackathon + Comet Opik
Setup Instructions:
-------------------
1. Install dependencies:
    pip install openai-agents opik python-dotenv
2. Set up OpenAI API key:
   Option A) Create a .env file in the project root:
    OPENAI_API_KEY=your_openai_key_here
    
   Option B) Export as environment variable:
    export OPENAI_API_KEY=your_openai_key_here
3. Configure Opik (for tracing and online evals):
    opik configure
   # Follow prompts for local server address
4. Run the script:
    python recipe_agent.py
References:
- Opik integration: https://www.comet.com/docs/opik/tracing/integrations/openai_agents
- OpenAI Agents SDK: https://platform.openai.com/docs/guides/agents
"""

import os
import asyncio
from dotenv import load_dotenv
from agents import Agent, Runner, set_trace_processors
from opik.integrations.openai.agents import OpikTracingProcessor

# Load environment variables from .env file
load_dotenv()

# Verify OpenAI API key is set
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY environment variable is not set")

# --- Agent 1: Recipe Suggester ---
RecipeSuggesterAgent = Agent(
    name="RecipeSuggester",
    instructions=(
        "You are a helpful chef. Given a list of ingredients, suggest a creative recipe. "
        "Be concise and clear. Output the recipe name and steps."
    ),
)

# --- Agent 2: Recipe Researcher ---
RecipeResearchAgent = Agent(
    name="RecipeResearcher",
    instructions=(
        "You are a research assistant. Given a recipe name, research and provide "
        "relevant information, tips, or variations for the recipe. Summarize your findings."
    ),
)

# --- Enable Opik Tracing ---
set_trace_processors(processors=[OpikTracingProcessor()])

# --- Demo Flow ---
async def main():
    print("Welcome to the Recipe Agent Demo!\n")
    ingredients = input("Enter a list of ingredients (comma-separated): ")

    # Step 1: Suggest a recipe
    recipe_result = await Runner.run(
        RecipeSuggesterAgent,
        f"Ingredients: {ingredients}"
    )
    recipe_name = recipe_result.final_output.split('\n')[0]  # Assume first line is recipe name

    print("\nSuggested Recipe:\n", recipe_result.final_output)

    # Step 2: Research the recipe
    research_result = await Runner.run(
        RecipeResearchAgent,
        f"Research the recipe: {recipe_name}"
    )
    print("\nRecipe Research:\n", research_result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
