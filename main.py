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




# TODO 4. Check resources sufficient?
# TODO 5. Process coins.
# TODO 6. Check transaction successful?
# TODO 7. Make Coffee

