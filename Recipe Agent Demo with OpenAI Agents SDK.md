![Recipe Agent Demo Architecture](https://i.imgur.com/41Ts9Qll.png)

# Recipe Agent Demo with OpenAI Agents SDK + Comet Opik

A simple demo showcasing the integration of [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/) with [Comet Opik](http://github.com/comet-ml/opik) for observability. This demo features two agents:

1. **RecipeSuggesterAgent**: Suggests recipes based on provided ingredients
2. **RecipeResearchAgent**: Researches additional information about the suggested recipe

## Setup

1. Install dependencies:
```bash
pip install openai-agents opik python-dotenv
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
python recipe_agent.py
```

## Features

- Multi-agent orchestration using OpenAI Agents SDK
- Asynchronous execution with proper error handling
- Integration with Comet Opik for tracing and observability
- Simple command-line interface for ingredient input

## Example Usage

```bash
Welcome to the Recipe Agent Demo!

Enter a list of ingredients (comma-separated): chicken, rice, soy sauce

Suggested Recipe:
[Recipe suggestion will appear here]

Recipe Research:
[Additional information will appear here]
```

## Project Structure

- `recipe_agent.py`: Main application file containing agent definitions and logic
- `.env`: (Optional) Environment variables file for API keys
