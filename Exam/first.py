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

def shopping():

    while True:
        wallet = input("How much money do you have in your pocket?").strip()
        if wallet.lower() == "done":
            print("You don't have money to spend.")
            return
        try:
            wallet_balance = float(wallet)  # We need to convert to number for calculations
            if wallet_balance < 0:
                print("Amounts can't be negative")
                continue
            break
        except ValueError:
            print("Please enter the valid numbers")

    total_spent = 0.0 # Tracking variable

    # Main loop for shopping
    while True:
        item_name = input("What would you like to buy? ").strip()
        #  Stop word "Done"
        if item_name.lower() == "done":
            break
        if item_name == "":
            print("Please enter an item name.")
            continue

        # Ask for item cost
        price_input = input("How much does it cost? ").strip()
        if price_input.lower() == "done":
            break  # allow stopping here too
        try:
            item_cost = float(price_input)  # convert to number for calculations
            if item_cost <= 0:
                print("Please enter a positive prices")
                continue
        except ValueError:
            print("Please enter a valid number plz")
            continue

         # Conditional check for checking if we can afford it or not.
        if item_cost <= wallet_balance:
            # Update wallet, and total cost
            wallet_balance -= item_cost
            total_spent += item_cost
            print(f"{item_name} was purchased for {format_amount(item_cost)}PLN. "
                  f"You have {format_amount(wallet_balance)}PLN left.")

            # If money is gone and is 0 you get break.
            if wallet_balance == 0: # Brokie counter
                print("You have run out of money.")
                break
        else:
            # Not affordable give error
            print(f"You don't have enough money to afford {item_name}.")
            print(f"You still have {format_amount(wallet_balance)}PLN left.")

    # Summary on your shopping
    print(f"Shopping complete. You have {format_amount(wallet_balance)}PLN remaining in your wallet, "
          f"you’ve spent {format_amount(total_spent)}PLN.")

def format_amount(x):
    """Helper to print whole numbers without .0, otherwise two decimals."""
    if float(x).is_integer():
        return str(int(x))
    return f"{x:.2f}"


if __name__ == "__main__":
    shopping()






#     # --- Initialize tracking variables ---
#     total_spent = 0.0  # how much has been spent in total

#     # --- Main shopping loop ---
#     while True:
#         item_name = input("What would you like to buy? ").strip()
#         # Case-insensitive stop word
#         if item_name.lower() == "done":
#             break
#         if item_name == "":
#             print("Please enter an item name.")
#             continue

#         # --- Ask for item cost (with validation) ---
#         price_input = input("How much does it cost? ").strip()
#         if price_input.lower() == "done":
#             break  # allow stopping here too
#         try:
#             item_cost = float(price_input)  # convert to number for calculations
#             if item_cost <= 0:
#                 print("Please enter a positive price.")
#                 continue
#         except ValueError:
#             print("Please enter a valid number (e.g., 3 or 2.99).")
#             continue

#         # --- Conditional check: can we afford it? ---
#         if item_cost <= wallet_balance:
#             # Update wallet and totals
#             wallet_balance -= item_cost
#             total_spent += item_cost
#             print(f"{item_name} was purchased for {format_amount(item_cost)}PLN. "
#                   f"You have {format_amount(wallet_balance)}PLN left.")

#             # Stop automatically if money is gone
#             if wallet_balance == 0:
#                 print("You have run out of money.")
#                 break
#         else:
#             # Not affordable: warn and do not subtract
#             print(f"You don't have enough money to afford {item_name}.")
#             print(f"You still have {format_amount(wallet_balance)}PLN left.")

#     # --- Final summary ---
#     print(f"Shopping complete. You have {format_amount(wallet_balance)}PLN remaining in your wallet, "
#           f"you’ve spent {format_amount(total_spent)}PLN.")

# def format_amount(x):
#     """Helper to print whole numbers without .0, otherwise two decimals."""
#     # W3Schools-style basics: use float methods and f-strings
#     if float(x).is_integer():
#         return str(int(x))
#     return f"{x:.2f}"

# # Standard Python main guard
# if __name__ == "__main__":
#     run_shopping()
