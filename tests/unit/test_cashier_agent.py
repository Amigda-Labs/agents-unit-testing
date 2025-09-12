import pytest
import asyncio

from dotenv import load_dotenv
from agents import Runner

from pizza_planet_agents.cashier_agent import cashier_agent

# ======== Cashier Agent Test Summary ========
# Cashier Agent be able to respond

# ======== How to Run ========
# Make sure you have OPENAI_API_KEY in the env file
# Run all tests: "uv run -m pytest -q"
# Run all tests with print statements: "uv run -m pytest -s"
# Run this specific file with pytest: "uv run -m pytest tests/test_cashier_agent.py -s"


def test_agent_response():
    """Agent should produce a non-empty greeting/response to a hello message."""
    async def run_cashier_agent():

        load_dotenv()

        user_message = "Hi there!" #Message sent to the cashier

        result = await Runner.run(
            starting_agent=cashier_agent,
            input= user_message
        )

        print("\n" + "=" * 30)
        print("[TEST] Cashier Agent Can Greet")
        print("-" * 30)
        print(f"Output:\n{result.final_output}")
        print("=" * 30 + "\n")

        assert result is not None
        assert isinstance(result.final_output, str)
        assert result.final_output.strip() != ""
    
    asyncio.run(run_cashier_agent())

