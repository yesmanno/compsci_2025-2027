import json
from datetime import datetime


def shopping(output_path="shopping_output.json"):
    purchases = []

    # --- Get starting pocket balance ---
    while True:
        pocket = input("How much money do you have in your pocket? ").strip()
        if pocket.lower() == "done":
            print("You don't have money to spend.")
            return

        try:
            pocket_balance = float(pocket)
            if pocket_balance < 0:
                print("Amounts can't be negative")
                continue
            break
        except ValueError:
            print("Please enter valid numbers")

    starting_balance = pocket_balance
    total_spent = 0.0

    # --- Main shopping loop ---
    while True:
        item_name = input("What would you like to buy? ").strip()

        if item_name.lower() == "done":
            break
        if item_name == "":
            print("Please enter an item name.")
            continue

        price_input = input("How much does it cost? ").strip()
        if price_input.lower() == "done":
            break

        try:
            item_cost = float(price_input)
            if item_cost <= 0:
                print("Please enter a positive price")
                continue
        except ValueError:
            print("Enter a valid number please")
            continue

        if item_cost <= pocket_balance:
            pocket_balance -= item_cost
            total_spent += item_cost
            purchases.append({"name": item_name, "cost": item_cost})

            print(
                f"{item_name} was purchased for {item_cost} PLN. "
                f"You have {pocket_balance} PLN left."
            )

            if pocket_balance == 0:
                print("You have run out of money.")
                break
        else:
            print(f"You don't have enough money to afford {item_name}.")
            print(f"You still have {pocket_balance} PLN left.")

    # --- Build output payload to save as JSON ---
    output_data = {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "currency": "PLN",
        "starting_balance": starting_balance,
        "total_spent": total_spent,
        "remaining_balance": pocket_balance,
        "purchases": purchases,
    }

    # --- Save JSON ---
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"\nSaved shopping summary to: {output_path}")

    with open(output_path, "r", encoding="utf-8") as f:
        saved = json.load(f)

    print("\n--- Reopened JSON (pretty) ---")
    print(json.dumps(saved, ensure_ascii=False, indent=2))

    print("\nReceipt")
    print(f"Time: {saved['timestamp']}")
    print(f"Starting: {saved['starting_balance']} {saved['currency']}")
    print("Items:")
    if saved["purchases"]:
        for p in saved["purchases"]:
            print(f"  - {p['name']}: {p['cost']} {saved['currency']}")
    else:
        print("  (none)")
    print(f"Spent: {saved['total_spent']} {saved['currency']}")
    print(f"Remaining: {saved['remaining_balance']} {saved['currency']}")


if __name__ == "__main__":
    shopping()
