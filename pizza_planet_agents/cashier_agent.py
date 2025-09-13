from agents import Agent
from agents import function_tool
from data.menu_data import get_menu_data

front_desk_instructions = "You are a friendly cashier serving in Pizza Planet"

@function_tool
def get_menu() -> str: 
    """Returns the comprehensive menu of Pizza Planet."""
    return get_menu_data()

@function_tool
def summarize_order() -> str:
    """Summarize the order and ask for validation"""

@function_tool
def calculate_total_order() -> str:
    """Compute the Total order and properly quantify them"""

cashier_agent=Agent(
    name = "Cashier agent",
    instructions = front_desk_instructions,
    model = "gpt-4o-mini", #Let's go for the cheapest one
    tools=[get_menu]
)