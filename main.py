MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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


# report
def report():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${remaining_money}")


# After the user enter a drink, check resources
# If something is in short supply, display a message
def check_resources(coffee_choice):
    if resources["water"] < MENU[coffee_choice]["ingredients"]["water"]:
        return False, "Sorry, there is not enough water."
    elif resources["milk"] < MENU[coffee_choice]["ingredients"]["milk"]:
        return False, "Sorry, there is not enough milk."
    elif resources["coffee"] < MENU[coffee_choice]["ingredients"]["coffee"]:
        return False, "Sorry, there is not enough coffee."
    return True, ""


# Calculate coins that the user inserted
def calculate_coins(quarters, dimes, nickles, pennies):
    coins = round(quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01, 2)
    return coins


# If the transaction is successful, ingredients should be deducted from resources
def make_coffee(coffee_choice):
    resources["water"] = resources["water"] - MENU[coffee_choice]["ingredients"]["water"]
    resources["milk"] = resources["milk"] - MENU[coffee_choice]["ingredients"]["milk"]
    resources["coffee"] = resources["coffee"] - MENU[coffee_choice]["ingredients"]["coffee"]
    # Display a message when coffee is ready
    print(f"Here is your {coffee_choice} Enjoy!")


# Initialize a variable to store money for report
remaining_money = 0


should_continue = True
while should_continue:
    # Prompt user by asking a drink they would like
    coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")

    # If the user enter "off", turn off the machines meaning end execution
    if coffee_choice == "off":
        should_continue = False
    # If the user enter "report", display a report
    elif coffee_choice == "report":
        report()
    else:
        is_sufficient, message = check_resources(coffee_choice)
        if is_sufficient:
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))

            # If the money is not enough, display a message and refund the money
            coins = calculate_coins(quarters, dimes, nickles, pennies)

            if coins < MENU[coffee_choice]["cost"]:
                print("Sorry, that's not enough money. Money refunded.")
            elif coins > MENU[coffee_choice]["cost"]:
                # If the money exceeds the price of the drink, offer change.
                change = round(coins - MENU[coffee_choice]["cost"], 2)
                print(f"Here is ${change} in change.")
                coins = coins - change
                # If the money is enough, add the money on a report
                remaining_money = round(remaining_money + coins, 2)
                make_coffee(coffee_choice)
            else:
                remaining_money = round(remaining_money + coins, 2)
                make_coffee(coffee_choice)
        else:
            print(message)





