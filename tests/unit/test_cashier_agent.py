import pytest
import asyncio

from dotenv import load_dotenv
from agents import Runner

#Agent to test:
from pizza_planet_agents.cashier_agent import cashier_agent 
#Agent Tester:
from tests.agent_tester import agent_tester, agent_tester_instructions

# ======== Cashier Agent Test Summary ========
# Cashier Agent be able to respond

# ======== How to Run ========
# Make sure you have OPENAI_API_KEY in the env file
# Run all tests: "uv run -m pytest -q"
# Run all tests with print statements: "uv run -m pytest -s"
# Run this specific file with pytest: "uv run -m pytest tests/unit/test_cashier_agent.py -s"


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

        # Test using Agent Tester
        tester_input = (
            "Evaluate if the following cashier response is friendly, clear, and appropriate.\n\n"
            f"Response: {result.final_output}"
        )
        tester_result = await Runner.run(
            starting_agent=agent_tester,
            input=tester_input
        )
        # Ensure tester ran without issues
        assert tester_result is not None
        
        # Use structured output directly
        output_obj = tester_result.final_output
        print(f"[TEST] Agent tester score: {getattr(output_obj, 'score', None)}")
        print(f"[TEST] Agent tester score: {getattr(output_obj, 'reasoning', None)}")
        assert hasattr(output_obj, "score"), "Agent tester did not return a score"
        assert isinstance(output_obj.score, int), "Agent tester score is not an integer"
        assert 3 <= output_obj.score <= 5, (
            f"Expected passing score between 3 and 5, got {output_obj.score}"
        )

    
    asyncio.run(run_cashier_agent())

