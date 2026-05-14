# Coffee Machine Program

MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 40,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 60,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 70,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources.get(item, 0):
            print(f"❌ Sorry, not enough {item}.")
            return False
    return True


def process_coins():
    print("Insert coins:")
    ten = int(input("₹10 coins: "))
    twenty = int(input("₹20 coins: "))
    fifty = int(input("₹50 coins: "))

    total = ten * 10 + twenty * 20 + fifty * 50
    return total


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"☕ Here is your {drink_name}. Enjoy!")


# Main Program
machine_on = True

while machine_on:
    choice = input("\nWhat would you like? (espresso/latte/cappuccino/report/off): ").lower()

    if choice == "off":
        machine_on = False

    elif choice == "report":
        print("\n📊 Resources:")
        for item in resources:
            print(f"{item}: {resources[item]}")
        print(f"Money: ₹{profit}")

    elif choice in MENU:
        drink = MENU[choice]

        if check_resources(drink["ingredients"]):
            payment = process_coins()

            if payment >= drink["cost"]:
                change = payment - drink["cost"]
                print(f"💰 Here is your change: ₹{change}")
                profit += drink["cost"]
                make_coffee(choice, drink["ingredients"])
            else:
                print("❌ Not enough money. Money refunded.")

    else:
        print("❌ Invalid choice.")