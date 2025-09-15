import pytest
import asyncio
import json

from dotenv import load_dotenv
from agents import Runner

#Agent to test:
from pizza_planet_agents.order_formatter_agent import order_formatter_agent 

# ======== Order Formatter Agent Test Summary ========
# Order Formatter Agent should be able to correctly parse an order,
# calculate subtotals for each item, and calculate the final total.

# ======== How to Run ========
# Make sure you have OPENAI_API_KEY in the env file
# Run all tests: "uv run -m pytest -q"
# Run all tests with print statements: "uv run -m pytest -s"
# Run this specific file with pytest: "uv run -m pytest tests/unit/test_order_formatter_agent.py -s"


def test_format_order_and_calculate_total():
    """Agent should correctly calculate subtotal and total for a given order."""
    async def run_order_formatter_agent():

        load_dotenv()

        # Order details
        order_details = """The customer ordered 3 medium cheese pizzas and 1 medium pepperoni pizza. 
        Cheese Pizza: 14 usd per unit
        Pepperoni Pizza: 16 usd per unit
        """
        
        # Expected values based on menu_data.py
        # Medium Cheese Pizza: $14
        # Medium Pepperoni Pizza: $16
        expected_cheese_subtotal = 3 * 14.00
        expected_pepperoni_subtotal = 1 * 16.00
        expected_total = expected_cheese_subtotal + expected_pepperoni_subtotal

        result = await Runner.run(
            starting_agent=order_formatter_agent,
            input= order_details
        )

        print("\n" + "=" * 30)
        print("[TEST] Order Formatter Agent Calculation")
        print("-" * 30)
        print(f"Output:\n{result.final_output}")
        print("=" * 30 + "\n")

        assert result is not None
        
        output_str = result.final_output
        assert isinstance(output_str, str)

        try:
            output_obj = json.loads(output_str)
        except json.JSONDecodeError:
            pytest.fail("The agent's output is not a valid JSON string.")

        assert "total" in output_obj, "The output is missing the 'total' field."
        assert output_obj["total"] == expected_total, f"Expected total to be {expected_total}, but got {output_obj['total']}"

        assert "items" in output_obj, "The output is missing the 'items' field."
        assert isinstance(output_obj["items"], list), "The 'items' field is not a list."
        
        # We can't guarantee the order of items, so we check them dynamically
        assert len(output_obj["items"]) == 2, f"Expected 2 items in the order, but got {len(output_obj['items'])}"

        cheese_item = next((item for item in output_obj["items"] if "cheese" in item.get("name", "").lower()), None)
        assert cheese_item is not None, "Cheese pizza not found in items."
        assert cheese_item.get("quantity") == 3
        assert cheese_item.get("subtotal") == expected_cheese_subtotal

        pepperoni_item = next((item for item in output_obj["items"] if "pepperoni" in item.get("name", "").lower()), None)
        assert pepperoni_item is not None, "Pepperoni pizza not found in items."
        assert pepperoni_item.get("quantity") == 1
        assert pepperoni_item.get("subtotal") == expected_pepperoni_subtotal

    
    asyncio.run(run_order_formatter_agent())
