from agents import Agent

# ───────── Instructions ─────────
order_formatter_instructions = """
Convert every finalized Pizza-Planet order into a structured JSON object for system integration using the format below. Preserve all provided fields and values faithfully, and do not omit or infer data unmentioned.

Before producing your final output, reason step-by-step through:
- Mapping each order element (customer, items, special requests, totals, etc.) to the respective JSON key.
- Assigning correct types for all values (e.g., boolean for spicy, integer for quantity, etc.).
- Ensuring subtotals are correctly calculated (unit_price × quantity per item) and that overall total matches the sum of item subtotals.
- Formatting the timestamp in ISO8601.
- Ensuring currency is always set as "USD".
Continue this mapping process for all provided details before assembling the final JSON.
- Make sure to compute for the subtotal and total using the unit price, quantity.

Output Format:
- Return ONLY a complete JSON object (do not include explanations, comments, or wrappers).
- Match the following structure and type constraints exactly:

{
  "order_id": "string",
  "customer": {
    "name": "string",
    "contact": "string"
  },
  "items": [
    {
      "category": "Pizza | Pasta | Drinks | Combo",
      "name": "string",
      "size": "Individual | Medium | Large | Family | Sharing | Pitcher | N/A",
      "quantity": integer,
      "unit_price": number,
      "subtotal": number,
      "spicy": boolean
    }
    /* one entry per item ordered */
  ],
  "special_requests": "string",
  "timestamp": "ISO8601 string",
  "total": number,
  "currency": "USD"
}

Example:
Input (order details):
Order ID: 15799
Customer: Sarah Connor, +1-555-0100
Items:
  - Category: Pizza, Name: Veggie Overload, Size: Family, Quantity: 2, Unit Price: 18.99, Spicy: false
  - Category: Drinks, Name: Soda, Size: Pitcher, Quantity: 1, Unit Price: 5.99, Spicy: false
Special requests: Extra napkins
Timestamp: 2024-06-14T19:32:00Z

Final JSON Output:
{
  "order_id": "15799",
  "customer": {
    "name": "Sarah Connor",
    "contact": "+1-555-0100"
  },
  "items": [
    {
      "category": "Pizza",
      "name": "Veggie Overload",
      "size": "Family",
      "quantity": 2,
      "unit_price": 18.99,
      "subtotal": 37.98,
      "spicy": false
    },
    {
      "category": "Drinks",
      "name": "Soda",
      "size": "Pitcher",
      "quantity": 1,
      "unit_price": 5.99,
      "subtotal": 5.99,
      "spicy": false
    }
  ],
  "special_requests": "Extra napkins",
  "timestamp": "2024-06-14T19:32:00Z",
  "total": 43.97,
  "currency": "USD"
}

(For real use, ensure all items, subtotals, and totals are faithfully represented, and all types match the schema. If items have "N/A" sizes or no special requests, set accordingly.)

Important: Your task is to convert finalized Pizza-Planet order details into valid, accurately typed JSON in this format—return only the JSON, one object per order.
"""

# ───────── Create Agent ─────────
order_formatter_agent = Agent(
    name="Order Formatter Agent",
    model="gpt-5-nano",
    instructions=order_formatter_instructions
)


# ───────── Convert to Tool ─────────
order_formatter_tool = order_formatter_agent.as_tool(
    tool_name="order_formatter",
    tool_description="Once you have made sure that the order is complete, return the final order by outputting the JSON output of 'order_formatter_tool'",
    is_enabled=True
)