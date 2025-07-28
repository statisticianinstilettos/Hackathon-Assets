#!/usr/bin/env python3
"""
Interactive Financial Advisor demo with proper Opik ADK integration.
This allows manual interaction while automatically tracking everything in Opik.
"""

import asyncio
import os
import uuid
from dotenv import load_dotenv

# Load environment variables first
load_dotenv()

from google.adk.runners import InMemoryRunner
from google.genai.types import Part, UserContent

# Import the agent (which now has Opik integration built-in)
from financial_advisor.agent import root_agent

async def run_interactive_demo():
    """Run an interactive Financial Advisor session with automatic Opik tracing"""
    
    print("🚀 Interactive Financial Advisor with Opik ADK Integration")
    print("=" * 65)
    print("This demo tracks your entire conversation automatically!")
    print("Type 'quit' to exit at any time.\n")
    
    # Check configuration
    api_key = os.getenv("OPIK_API_KEY")
    workspace = os.getenv("OPIK_WORKSPACE")
    gemini_key = os.getenv("GOOGLE_API_KEY")
    
    if not gemini_key:
        print("❌ Error: GOOGLE_API_KEY not found in environment variables")
        print("Please add your Gemini API key to the .env file")
        return
    
    if not api_key or api_key == "your_opik_api_key_here":
        print("⚠️  Warning: OPIK_API_KEY not configured")
        print("Opik tracing will be disabled. Add your API key to .env for tracing.")
    else:
        print(f"✅ Opik configured for workspace: {workspace}")
    
    # Generate a unique conversation ID
    conversation_id = str(uuid.uuid4())
    print(f"📊 Conversation ID: {conversation_id}")
    print("🔗 Check your Opik dashboard to see traces in real-time!\n")
    
    # Initialize the runner with our Opik-instrumented agent
    runner = InMemoryRunner(agent=root_agent)
    session = await runner.session_service.create_session(
        app_name=runner.app_name, 
        user_id="interactive_user"
    )
    
    step = 0
    
    try:
        while True:
            step += 1
            
            # Get user input
            print(f"\n--- Step {step} ---")
            user_input = input("💬 You: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("👋 Goodbye!")
                break
            
            if not user_input:
                print("Please enter a message or 'quit' to exit.")
                step -= 1  # Don't count empty inputs
                continue
            
            # Create message content
            content = UserContent(parts=[Part(text=user_input)])
            
            print("🤖 Agent: ", end="", flush=True)
            
            # Run the agent - Opik tracing happens automatically via ADK integration
            try:
                for event in runner.run(
                    user_id=session.user_id,
                    session_id=session.id,
                    new_message=content
                ):
                    for part in event.content.parts:
                        if hasattr(part, 'text') and part.text:
                            print(part.text, end="", flush=True)
                
                print("\n")  # New line after response
                
            except Exception as e:
                print(f"\n❌ Error: {str(e)}")
                import traceback
                traceback.print_exc()
            
    except KeyboardInterrupt:
        print("\n\n⏹️  Session interrupted by user (Ctrl+C)")
    
    print(f"\n{'='*65}")
    print("✅ Session completed!")
    print(f"📊 Total exchanges: {step}")
    print(f"🔗 Conversation ID: {conversation_id}")
    print("📈 All traces automatically logged via ADK integration!")
    print("Check your Opik dashboard to see all the traces!")

def main():
    """Main function with setup checks"""
    
    # Check environment setup
    if not os.getenv("GOOGLE_API_KEY"):
        print("❌ Error: GOOGLE_API_KEY not found in environment variables")
        print("Please add your Gemini API key to the .env file")
        return
    
    print("✅ Using official ADK integration with OpikTracer")
    
    try:
        asyncio.run(run_interactive_demo())
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("Make sure all environment variables are set correctly in .env file")

if __name__ == "__main__":
    main() 