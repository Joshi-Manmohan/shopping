# Concession Program

menu = {
    "pizza": 3.00,
    "nachos": 4.00,
    "popcorn": 5.00,
    "fries": 1.00,
    "chips": 2.00,
    "aalu": 3.50,
    "soda": 2.00,
    "lemon": 2.50,
}

cart = []
total = 0

print("---------- MENU ----------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("--------------------------")

while True:
    food = input("Select item (q to quit): ").lower()
    if food == "q":
        break
    elif food in menu:
        cart.append(food)
        print(f"Added {food} to your cart.")
    else:
        print("Item not found. Please select a valid item.")

print("\n------- YOUR ORDER ---------")
for food in cart:
    total += menu[food]
    print(food.capitalize(), end=", ")
print(f"\nTotal is: ${total:.2f}")

