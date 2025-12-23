menu = {
    "pizza" :40,
    "pasta" :60,
    "burger" :50,
    "salad" :30,
    "coffee" :80,
    "tea" :70,
    "soup" :45,
    "sandwich" :55,
    "dessert" :90,
    "juice" :65,
    "water" :20,
}

print("Welcome to the Hotel Menu!")
print("Here is our menu:")
for item, price in menu.items():
    print(f"{item}: ${price}")
total_price= 0
item_1=input("Please enter the item you want to order: ")
if item_1 in menu:
    total_price += menu[item_1]
    print(f"Total price for {item_1} is: ${total_price}")
else:
    print("Item not found in the menu. Please try again.")
another_order = input("Do you want to order another item? (yes/no): ")
if another_order == "yes":
    item_2 = input("Please enter the next item you want to order: ")
    if item_2 in menu:
        total_price += menu[item_2]
        print(f"Total price for {item_2} is: ${total_price}")
    else:
        print("Item not found in the menu. Please try again.")
print(f"the total amount of items to pay is: ${total_price}")
print("Thank you for your order!")
