#!/usr/bin/env python3
"""
Demo script for running Financial Advisor with proper Opik ADK integration.
This uses the official OpikTracer approach from the documentation.
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

async def run_financial_advisor_demo():
    """Run a complete Financial Advisor demo with proper Opik tracing"""
    
    print("🚀 Starting Financial Advisor Demo with Opik ADK Integration...")
    print("=" * 65)
    
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
    
    # Generate a unique conversation ID for this demo
    conversation_id = str(uuid.uuid4())
    print(f"📊 Conversation ID: {conversation_id}")
    
    # Initialize the runner with our Opik-instrumented agent
    runner = InMemoryRunner(agent=root_agent)
    session = await runner.session_service.create_session(
        app_name=runner.app_name, 
        user_id="demo_user"
    )
    
    # Demo conversation flow
    demo_messages = [
        "Hello! I'd like to get financial advice.",
        "AAPL",  # Stock ticker
        "moderate risk, long-term investment",  # Risk profile
        "no particular execution preferences",  # Execution preferences
        "proceed"  # Final confirmation
    ]
    
    print("\n🎯 Starting Multi-Agent Financial Advisory Process...")
    print("📈 Each step will be automatically traced by Opik ADK integration\n")
    
    for i, message in enumerate(demo_messages, 1):
        print(f"--- Step {i}: User Message ---")
        print(f"💬 User: {message}")
        
        # Create message content
        content = UserContent(parts=[Part(text=message)])
        
        print("🤖 Agent: ", end="", flush=True)
        
        # Run the agent - Opik tracing happens automatically via callbacks
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
            print(f"\n❌ Error during agent execution: {e}")
            import traceback
            traceback.print_exc()
        
        # Small delay between steps for readability
        await asyncio.sleep(1)
    
    print("\n" + "=" * 65)
    print("✅ Demo completed!")
    print(f"🔗 Conversation ID: {conversation_id}")
    print("📊 All traces automatically logged to Opik via ADK integration")
    print("🎯 Check your Opik dashboard to see:")
    print("   • Complete conversation flow")
    print("   • Individual agent traces (data analyst, trading analyst, etc.)")
    print("   • Tool usage (Google Search calls)")
    print("   • Cost tracking and performance metrics")
    print("   • Session threading for conversation continuity")

if __name__ == "__main__":
    try:
        asyncio.run(run_financial_advisor_demo())
    except KeyboardInterrupt:
        print("\n\n⏹️  Demo stopped by user (Ctrl+C)")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        print("Make sure all environment variables are set correctly in .env file") 