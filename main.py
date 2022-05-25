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

def get_change():
    global change
    if money == cost(user_input):
        return True
    elif money > cost(user_input):
        change = round(money - cost(user_input), 2)
        return True
    else:
        return False
        print("Sorry that's not enough money. Money refunded")

def ask_money():
    global money
    # TODO 5. Process coins.
    q = float(input("how many quarters?"))
    d = float(input("how many dimes?"))
    n = float(input("how many nickles?"))
    p = float(input("how many pennies?"))
    money = cal_coins(q, d, n, p)

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

flag = False

while flag == False:

    # TODO 2. Turn off the Coffee Machine by entering “off” to the prompt.

    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    if user_input == "off":
        flag = True
        break
    if user_input == "report":
        get_resources()

    if user_input == "espresso":
        if enough_resources(user_input) == True:
            ask_money()
            if get_change() == True:
                resources["water"] -= MENU["espresso"]["ingredients"]["water"]
                resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
                print(f"Here is your {user_input}")
            else:
                pass
    elif user_input == "latte":
        if enough_resources(user_input) == True:
            ask_money()
            if get_change() == True:
                    resources["water"] -= MENU["latte"]["ingredients"]["water"]
                    resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
                    resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
                    print(f"Here is your {user_input}")
            else:
                pass
    elif user_input == "cappuccino":
        if enough_resources(user_input) == True:
            ask_money()
            if get_change() == True:
                    resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
                    resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
                    resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
                    print(f"Here is your {user_input}")
            else:
                pass
    # print(resources)
    # print(change)
    # print(user_input)
    # print(get_change())
    if change != 0:
        print(f"Here is {change} dollars in change.")
        change = 0

