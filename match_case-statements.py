# Match-case statements in Python
# Match-case statements are used to match patterns in data structures.        
def order_food(item):
    match item.lower():
        case "burger":
            return "burger's price is of ₹80"
        case "pizza":
            return "pizza's price is of ₹250"
        case "momo":
            return "momo's price is of ₹100"
        case "ice cream":
            return "ice cream's price is of ₹100"
        case "cold drink":
            return "cold drink's price is of ₹50"
        case _:
            return "Sorry, item not available."
# Example usage:
user_input = input("Enter you order (Burger/Pizza/Momo/Ice Cream/Cold Drink): ")
print(order_food(user_input))
item_price = order_food(user_input)
confirm = input("confirm your order (yes/no): ") 
if (confirm.lower() == "yes"):
    print("Your order has been confirmed.")
    print("Thank you for your order! Your order will be delivered soon.")
elif (confirm.lower() == "no"):
    print("Your order has been cancelled.")
    print("Thank you for visiting our restaurant!")
else:
    print("Invalid input. Please enter 'yes' or 'no'.")
# The match-case statement is used to match the user's input with the available items.
