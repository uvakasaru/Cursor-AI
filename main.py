import asyncio
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from agents import Agent, Runner, set_trace_processors
from langsmith.integrations.openai_agents_sdk import OpenAIAgentsTracingProcessor



load_dotenv()

from langchain.agents import create_agent


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


agent = create_agent(
    model="openai:gpt-5.4",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)
    

async def main():
    print(f"Tracing enabled: {os.getenv('LANGCHAIN_TRACING_V2')}")    
    print(os.environ.get("OPENAI_API_KEY"))    
    print("Hello from cursor-ai!")

    # Run the agent
    response = agent.invoke(
        {"messages": [{"role": "user", "content": "What is the weather in McKinney TX?"}]}

    )
    print(response)
if __name__ == "__main__":
    set_trace_processors([OpenAIAgentsTracingProcessor()])
    asyncio.run(main())
