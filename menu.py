MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

is_on = True
profit = 0


def enough_resources(ingredients):
    for i in ingredients:
        if ingredients[i] >= resources[i]:
            print(f"Sorry, we do not have enough {i}")
            return False
    return True


def collect_money():
    print("insert coins >> ")
    total = int(input("How many quarters? >> ")) * 0.25
    total += int(input("How many quarters? >> ")) * 0.10
    total += int(input("How many quarters? >> ")) * 0.05
    total += int(input("How many quarters? >> ")) * 0.01
    return total


def transaction_successful(price, payment):
    if payment >= price:
        change = round(payment - price, 3)
        print(f"Here is your change ${change}")
        global profit
        profit += price
        return True
    else:
        print("Sorry, you have not enough monet")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if enough_resources(drink["ingredients"]):
            payment = collect_money()
            if transaction_successful(drink["cost"],payment):
                make_coffee(choice, drink["ingredients"])


