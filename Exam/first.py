# Programming Task

# You are going to write a Python program that simulates buying items with the money you have in your wallet. YOU CAN USE W3 SCHOOLS SPECIFICALLY SYNTAX
# Steps
# Your program must:
# Start by asking the user how much money they have in their wallet.
# Allow the user to purchase items one by one until they either:
# Type "done" to stop shopping, or
# Run out of money completely.
# For each purchase:
# Ask what item they are buying.
# Ask how much it costs.
# If they can afford it, subtract the price from their wallet and confirm the purchase.
# If they cannot afford it, print a warning message and do not subtract the money.
# The program must handle the user input in a case-insensitive way for "done" (e.g., "Done", "DONE", "done" should all stop the program).
# The program should use a function that contains your main logic (loop, conditions, and calculations).
# After the user is finished shopping or runs out of money, print the final amount of money left in their wallet, as well as how much they’ve spent.
# Requirements
# Your solution must:
# Contain at least one user-defined function
# Correctly convert data types into suitable types for calculations
# Use a loop to continue asking for input.
# Use conditional statements to check if purchases are affordable.
# Use string methods to manage user input.
# Include comments that describe each major section of your code. (loop, conditional check etc.)
# Follow naming conventions (meaningful variable and function names, e.g. wallet_balance, item_cost).

# Example Output/Input
# How much money do you have in your pocket?(input) 50
# What would you like to buy?(input) apple
# How much does it cost?(input) 3
# apple was purchased for 3PLN. You have 47PLN left.
# What would you like to buy?(input) chocolate
# How much does it cost?(input) 10
# chocolate was purchased for 10PLN. You have 37PLN left.
# What would you like to buy?(input) headphones
# How much does it cost?(input) 60
# You don't have enough money to afford headphones.
# You still have 37PLN left.
# What would you like to buy? done
# Shopping complete. You have 37PLN remaining in your wallet, you’ve spent 23PLN.

def wallet():
    total = 0.0
    item_count = 0

    while True:
        wallet = input("How much money do you have in your pocket?(input)").strip()
        if wallet.lower() == "done":
            break

        # Some basic validation
        while True:
            try:
                price_str = input(f"How much does {thing} this thing cost?").strip()
                price = float(price_str)
                break
            except ValueError:
                print("This is a wrong number, please add correct number")

if __name__ == "__main__":
    wallet()


