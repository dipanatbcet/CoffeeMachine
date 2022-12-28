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
    "water": 1000,
    "milk": 200,
    "coffee": 100,
}
#consumed_water = 0
#consumed_milk = 0
#consumed_coffee = 0
consumption = {"water":0,"milk":0,"coffee":0}


def machine_stock(resources, consumption):
    available_stock={}
    available_stock['available_water'] = resources['water'] - consumption["water"]
    available_stock['available_milk'] = resources['milk'] - consumption["milk"]
    available_stock['available_coffee'] = resources['coffee'] - consumption["coffee"]
    return available_stock

user_selected = {}
def stock_availability(user_selected):
    availability = False
    available_stock = machine_stock(resources, consumption)
    if available_stock['available_water']>=user_selected["water"]:
        if available_stock['available_milk']>=user_selected["milk"]:
            if available_stock['available_coffee']>=user_selected["coffee"]:
                availability = True
                #print('ok')
            else:
                print("Sorry there is not enough coffee.")
        else:
            print("Sorry there is not enough milk.")
    else:
        print("Sorry there is not enough water.")
    return availability


machine_balance = 0
machine_continue =True
while machine_continue:
    user_choice = input('What would you like? (espresso/latte/cappuccino):').lower()
# TODO 1 Print machine stock
    if user_choice == 'report':
        #available_stock = machine_stock(resources, consumption)
        print(f'Water:{resources["water"]}\nMilk:{resources["milk"]}\nCoffee:{resources["coffee"]}')
        print(f"Money:${machine_balance}")
    # TODO 2 check stock
    elif user_choice == 'espresso':
        choice1 = MENU["espresso"]
        choice1['ingredients']['milk'] = 0
        stock_check = stock_availability(choice1["ingredients"])
    elif user_choice == 'latte':
        choice1 = MENU["latte"]
        #stock_availability(choice1["ingredients"])
        stock_check = stock_availability(choice1["ingredients"])
    elif user_choice == 'cappuccino':
        choice1 = MENU["cappuccino"]
        #stock_availability(choice1["ingredients"])
        stock_check = stock_availability(choice1["ingredients"])

    # TODO 3 process coins + profit balance increase
    if user_choice !='off':
        if user_choice !='report' and stock_check == True:
            print("Please insert coins.")
            qtr = float(input('how many quarters?:'))
            dimes = float(input('how many dimes?:'))
            nickels = float(input('how many nickels?:'))
            penny = float(input('how many pennies?:'))
            total = round((qtr*.25 + dimes*.10 + nickels*.05 + penny*.01),2)
        # TODO 4 check transaction
            if total >= choice1['cost']:
                print(f"Here is ${round(total-choice1['cost'],2)} in change.")
                machine_balance += choice1['cost']
                coffeemake = True
            elif total < choice1['cost']:
                print("Sorry that's not enough money. Money refunded.")
                coffeemake = False
                machine_continue = False
            else:
                coffeemake = True
                machine_balance += total
        # TODO 5 coffee process and stock update
            if coffeemake == True:
                #d = choice1['ingredients']['water']
                consumption["water"] = choice1['ingredients']['water']
                consumption["milk"] = choice1['ingredients']['milk']
                consumption["coffee"] = choice1['ingredients']['coffee']
                resources_1 = machine_stock(resources, consumption)
                resources['water'] = resources_1['available_water']
                resources['milk'] = resources_1['available_milk']
                resources['coffee'] = resources_1['available_coffee']

                print(f"Take your {user_choice}☕️")
                #print(resources)
                #print(consumption)
                #print(f'Water:{available_stock["available_water"]}\nMilk:{available_stock["available_milk"]}\nCoffee:{available_stock["available_coffee"]}')
        elif user_choice == 'report':
            machine_continue = True
        else:
            machine_continue = False
    else:
        machine_continue = False