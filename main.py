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

money = 0
QUARTERS = 0.25
DIMES = 0.10
NICKLES = 0.05
PENNIES = 0.01
change = 0


def get_resources():
    print(f"Water: {resources.get('water')}ml")
    print(f"Milk: {resources.get('milk')}ml")
    print(f"Coffee: {resources.get('coffee')}g")


def cost(coffee):
    """THis function will identify the cost of each coffee"""
    if coffee == "espresso":
        return MENU["espresso"]["cost"]
    elif coffee == "latte":
        return MENU["latte"]["cost"]
    elif coffee == "cappuccino":
        return MENU["cappuccino"]["cost"]


def cal_coins(quarter, dime, nickle, penny):
    """Takes number of coins and returns total coin value"""
    quarter = quarter * QUARTERS
    dime = dime * DIMES
    nickle = nickle * NICKLES
    penny = penny * PENNIES
    return quarter + dime + nickle + penny

def enough_resources(coffee_type):
    if coffee_type != "espresso":
        if resources["water"] < MENU[coffee_type]["ingredients"]["water"]:
            print("Sorry there is not enough water")
            return False
        elif resources["milk"] < MENU[coffee_type]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee")
            return False
        elif resources["milk"] < MENU[coffee_type]["ingredients"]["milk"]:
            print("Sorry there is not enough milk")
            return False
        else:
            return True
    elif coffee_type == "espresso":
        if resources["water"] < MENU[coffee_type]["ingredients"]["water"]:
            print("Sorry there is not enough water")
            return False
        elif resources["milk"] < MENU[coffee_type]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee")
            return False
        else:
            return True
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):
# TODO 2. Turn off the Coffee Machine by entering “off” to the prompt.

# user_input = input("What would you like? (espresso/latte/cappuccino): ")


# # TODO 3. Print report
#
# if user_input == "report":
#     get_resources()
user_input = "espresso"
# print(enough_resources("cappuccino"))
# TODO 4. Check resources sufficient?


# if user_input == "espresso":
#     if enough_resources(user_input) == True:
#         resources["water"] -= MENU["espresso"]["ingredients"]["water"]
#         resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
#
# elif user_input == "latte":
#     if enough_resources(user_input) == True:
#         resources["water"] -= MENU["latte"]["ingredients"]["water"]
#         resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
#         resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
# elif user_input == "cappuccino":
#     if enough_resources(user_input) == True:
#         resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
#         resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
#         resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
# print(resources)

# TODO 5. Process coins.
q = float(input("how many quarters?"))
d = float(input("how many dimes?"))
n = float(input("how many nickles?"))
p = float(input("how many pennies?"))
money = cal_coins(q, d, n, p)
print(money)
print(cost(user_input))
if money == cost(user_input):
    print("Perfect money")
elif money > cost(user_input):
    change = round(money - cost(user_input),2)
    print(change)
else:
    print("Sorry that's not enough money. Money refunded")

# TODO 6. Check transaction successful?
# TODO 7. Make Coffee
