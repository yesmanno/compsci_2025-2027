def juice_bar():
    print("Welcome to FreshWave Juice Bar!")
    total = 0.0
    item_count = 0
    items = []

    while True:
        juice = input("What juice would you like to order?").strip()
        if juice.lower() == "done":
            break

        # Some basic validation
        while True:
            try:
                price_str = input(f"How much does {juice} juice cost?").strip()
                price = float(price_str)
                break
            except ValueError:
                print("Please enter a valid number")

        total += price
        item_count += 1
        items.append((juice, price))

        print(f"{juice} was added for {price} dollars.")
        print(f"Your total so far is: {total} dollars.")

    print(f"Thank you for your order! Your total is: {total} dollars.")
    print(f"Items ordered: {item_count}")

    if items:
        print("Order summary:")
        for name, price in items:
            print(f" - {name}: {price} dollars")

if __name__ == "__main__":
    juice_bar()
