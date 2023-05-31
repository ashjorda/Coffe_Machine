from machine_data import resources, MENU

menu_selection = MENU
ingredient_resources = resources
def ingredient_check(selected_drink):
    """Checks ingredient levels for selected drink"""
    selection_ingredients = menu_selection[selected_drink]["ingredients"]

    if selected_drink == "espresso":
        if ingredient_resources["water"] < selection_ingredients["water"]:
            print("Sorry there is not enough water.")
            if ingredient_resources["coffee"] < selection_ingredients["coffee"]:
                print("Sorry, there is not enough coffee.")
        else:
            ingredient_resources["water"] -= selection_ingredients["water"]
            ingredient_resources["coffee"] -= selection_ingredients["coffee"]
            return "collect money"
    elif selected_drink == "latte":
        if ingredient_resources["water"] < selection_ingredients["water"]:
            print("Sorry there is not enough water.")
            if ingredient_resources["coffee"] < selection_ingredients["coffee"]:
                print("Sorry, there is not enough coffee.")
                if ingredient_resources["milk"] < selection_ingredients["milk"]:
                    print("Sorry, there is not enough water.")
        else:
            ingredient_resources["water"] -= selection_ingredients["water"]
            ingredient_resources["coffee"] -= selection_ingredients["coffee"]
            ingredient_resources["milk"] -= selection_ingredients["milk"]
            return "collect money"
    elif selected_drink == "cappuccino":
        if ingredient_resources["water"] < selection_ingredients["water"]:
            print("Sorry there is not enough water.")
            if ingredient_resources["coffee"] < selection_ingredients["coffee"]:
                print("Sorry, there is not enough coffee.")
                if ingredient_resources["milk"] < selection_ingredients["milk"]:
                    print("Sorry, there is not enough water.")
        else:
            ingredient_resources["water"] -= selection_ingredients["water"]
            ingredient_resources["coffee"] -= selection_ingredients["coffee"]
            ingredient_resources["milk"] -= selection_ingredients["milk"]
            return "collect money"

def check_applepay(selected_drink):
    print("Please insert coins:")
    quarters = float(input("How many quarters: "))
    dimes = float(input("How many dimes: "))
    nickles = float(input("How many nickles: "))
    pennies = float(input("How many pennies: "))

    drink_cost = menu_selection[selected_drink]["cost"]
    applepay = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * .01)

    if applepay == drink_cost:
        print(f"Here is your {selected_drink}. Enjoy!")
        return drink_cost
    elif applepay > drink_cost:
        change = format((applepay - drink_cost), ".2f")
        print(f"Here is {change} in change.\nHere is your {selected_drink}. Enjoy!")
        return drink_cost
    else:
        print("Sorry that's not enough money. Money refunded.")

def machine_report(profit):
    profit = format(profit, ".2f")
    print("Water: " + str(ingredient_resources["water"]) + "ml")
    print("Milk: " + str(ingredient_resources["milk"]) + "ml")
    print("Coffee: " + str(ingredient_resources["coffee"]) + "g")
    print(f"Money: ${profit}")

def create_drink(selected_drink):
    if ingredient_check(selected_drink) == "collect money":
        paid_amount = check_applepay(selected_drink)
        return paid_amount
    else:
        return 0

machine_state = True
profit = float(0)

#Start of the Application
while machine_state:
    print("~~~~~~~~~Menu~~~~~~~~~\nEspresso: $1.50\nLatte: $2.50\nCappuccino: $3.00")
    selected_drink = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()

    if selected_drink == 'off':
        machine_state = False
    elif selected_drink == 'report':
        machine_report(profit)
    elif selected_drink in ['espresso', 'latte', 'cappuccino']:
        profit += create_drink(selected_drink)
    else:
        print("Incorrect Menu Option Entered")


