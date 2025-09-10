from agents import Agent
from agents import function_tool

front_desk_instructions = "You are a friendly cashier serving in Pizza Planet"

@function_tool
def get_menu() -> str: 
    """Returns the menu of pizza planet."""
    return "1. Cheese Pizza - $2 \n2. Pepperoni Pizza - $4\n3. Veggie Pizza - $3\n4. Soda - $1"

cashier_agent=Agent(
    name = "Cashier agent",
    instructions = front_desk_instructions,
    model = "gpt-4o-mini", #Let's go for the cheapest one
    tools=[get_menu]
)