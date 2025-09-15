from agents import Agent
from agents import function_tool

from data.menu_data import get_menu_data

#Import Tools
from pizza_planet_agents.order_formatter_agent import order_formatter_tool


front_desk_instructions = """
You are a friendly cashier serving in Pizza Planet.
When asked for the menu, do not show the full menu unless asked to. Example, if the customer is only interested in pizza, show only pizza.
Once you have made sure that the order is complete, return the final order by outputting the JSON output of 'order_formatter_tool'.
"""

@function_tool
def get_menu() -> str: 
    """Returns the comprehensive menu of Pizza Planet."""
    return get_menu_data()


cashier_agent=Agent(
    name = "Cashier agent",
    instructions = front_desk_instructions,
    model = "gpt-5-nano",
    tools=[get_menu, order_formatter_tool]
)