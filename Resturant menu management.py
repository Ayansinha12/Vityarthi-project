m = {
    1: {"name": "Chicken tikka", "price": 1500},
    2: {"name": "Dosa", "price": 870},
    3: {"name": "white sauce pasta", "price": 1800},
    4: {"name": "steamed broccoli", "price": 900},
    5: {"name": "Two ocean sauvignon Blanc(G)", "price": 3555},
    6: {"name": "tiramisu", "price": 2300},
    7: {"name": "Gillafi mutton seekh", "price": 2100},
    8: {"name": "Pearl barley Risotto", "price": 6500}
}

def show_m():
    print("\n--- Menu ---")
    for key, item in m.items():
        print(f"{key}. {item['name']} - ₹{item['price']}")

def take_order():
    order = []
    while True:
        show_m()
        choice = input("\nEnter the number of the item to order (or 'done' to finish): ")
        if choice.lower() == 'done':
            break
        try:
            item_n = int(choice)
            if item_n in m:
                order.append(m[item_n])
                print(f"{m[item_n]['name']} added to your order.")
            else:
                print("Invalid item number. Please try again.")
        except ValueError:
            print("Please enter a valid number or 'done'.")
    return order

def calculate_total(order):
    total = sum(item['price'] for item in order)
    return total

def print_bill(order):
    print("\n--- Order bill ---")
    for item in order:
        print(f"{item['name']} - ₹{item['price']}")
    total = calculate_total(order)
    print(f"Total: ₹{total}")

def main():
    print("Welcome to the Panache Food Ordering App!")
    order = take_order()
    if order:
        print_bill(order)
        print("\nThank you for your order and please do rate our service!")
    else:
        print("No items ordered. Have a good day!")

if __name__ == "__main__":
    main()
