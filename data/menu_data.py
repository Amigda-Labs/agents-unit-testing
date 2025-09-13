"""
Menu data for Pizza Planet.
This module contains the hardcoded menu data that will eventually be replaced
with database queries. Keeping it separate makes the transition easier.
"""

PIZZA_PLANET_MENU = """
🍕 PIZZA PLANET MENU 🍕

═══════════════════════════════════════════════════════════════
🍕 PIZZAS
═══════════════════════════════════════════════════════════════
Individual (Personal) | Medium (2-3 people) | Large (4-5 people)

Classic Pizzas:
• Cheese Pizza              $8  | $14  | $18
• Pepperoni Pizza           $10 | $16  | $22
• Veggie Supreme            $12 | $18  | $24
• Hawaiian (Ham & Pineapple) $11 | $17  | $23

Spicy Pizzas: 🌶️
• Spicy Pepperoni           $12 | $18  | $25
• Hot Buffalo Chicken       $14 | $20  | $27
• Jalapeño Fire             $13 | $19  | $26
• Devil's Delight (Extra Hot) $15 | $21  | $28

Sharing Pizzas (Serves 6-8):
• Giant Meat Lovers         $32
• Mega Veggie Deluxe        $30
• Spicy Supreme Feast 🌶️    $35
• Ultimate Everything       $38

═══════════════════════════════════════════════════════════════
🍝 PASTA
═══════════════════════════════════════════════════════════════
Individual | Family Size (3-4 people)

Classic Pasta:
• Spaghetti Marinara        $9  | $16
• Fettuccine Alfredo        $12 | $20
• Penne Arrabbiata 🌶️       $11 | $18
• Lasagna Classica          $14 | $24

Spicy Pasta: 🌶️
• Spicy Cajun Chicken Pasta $15 | $26
• Hot Italian Sausage Penne $14 | $23
• Diavolo Linguine          $13 | $22
• Fire Dragon Pasta         $16 | $28

Sharing Pasta (Serves 5-6):
• Family Spaghetti & Meatballs $28
• Giant Baked Ziti             $25
• Spicy Seafood Linguine 🌶️    $32

═══════════════════════════════════════════════════════════════
🥤 DRINKS
═══════════════════════════════════════════════════════════════
Individual | Pitcher (Serves 4-6)

Soft Drinks:
• Coca-Cola, Pepsi, Sprite  $3  | $12
• Lemonade                  $3  | $12
• Iced Tea                  $3  | $12

Specialty Drinks:
• Italian Soda              $4  | $15
• Fresh Fruit Smoothies     $6  | $22
• Milkshakes               $5  | N/A

Hot Beverages:
• Coffee                    $3
• Hot Chocolate             $4
• Italian Espresso          $4

═══════════════════════════════════════════════════════════════
🍕🍝 COMBO SPECIALS (Like Sbarro!)
═══════════════════════════════════════════════════════════════

Personal Combos:
• Pizza Slice + Pasta Bowl + Drink    $15
• 2 Pizza Slices + Drink              $12
• Pasta Bowl + Garlic Bread + Drink   $13

Family Combos:
• Medium Pizza + Family Pasta + Pitcher Drink  $35
• Large Pizza + 2 Pasta Bowls + 4 Drinks      $42
• 2 Medium Pizzas + Family Pasta + Pitcher     $45

Sharing Feast Combos:
• Giant Pizza + Sharing Pasta + 2 Pitchers     $65
• 2 Large Pizzas + 2 Family Pastas + 3 Pitchers $85
• Ultimate Feast: Everything Combo for 10 people $120

═══════════════════════════════════════════════════════════════
🌶️ = Spicy Item | All prices in USD
Serving sizes are estimates. Sharing options available for groups!
═══════════════════════════════════════════════════════════════
""".strip()


def get_menu_data() -> str:
    """
    Returns the current menu data.
    
    This function serves as an abstraction layer that will make it easy
    to switch from hardcoded data to database queries in the future.
    
    Future implementation might look like:
    # from .database import fetch_current_menu
    # return fetch_current_menu()
    """
    return PIZZA_PLANET_MENU
