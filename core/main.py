#Step 1: Import OpenAI Agents SDK
from agents import Agent

#Step 2: Test communication with the agent prototype using REPL
from dotenv import load_dotenv      # Loads up the keys needed in order to communicate
import asyncio                      # Python's toolkit for async programming
from agents import run_demo_loop    # nteractive testing of an agent's behavior directly in your terminal

#Step 3: Refactor file structure
from pizza_planet_agents.cashier_agent import cashier_agent


# ======= How to Run =======
# Since we placed main in the core folder,  "uv run core/main.py"
# ==========================

load_dotenv()

async def main():
    await run_demo_loop(cashier_agent)

if __name__ == "__main__":
    asyncio.run(main())
