#Ioannis Apomachos
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



def print_report(money,resources):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def check_water(water):
    if water>=MENU[user_choice]['ingredients']['water']:
        return True
    else:
        print("Sorry there is not enough water.")
        return False

def check_milk(milk):
    if milk>=MENU[user_choice]['ingredients']['milk']:
         return True
    else:
        print("Sorry there is not enough milk.")
        return False
    

def check_coffee(coffee): 
    if coffee>=MENU[user_choice]['ingredients']['coffee']:
         return True
    else:
        print("Sorry there is not enough coffee.")
        return False


def process_coins():
    print("Please insert coins.")
    quarters=int(input("How many quarters?: "))
    dimes=int(input("How many dimes?: "))
    nickles=int(input("How many nickles?: "))
    pennies=int(input("How many pennies?: "))

    money=0.25*quarters + 0.10*dimes + 0.05*nickles + 0.1*pennies
    return money



def check_resources(user_choice,resources):
    milk_status=True

    water_status=check_water(resources['water'])
    if water_status:
        if user_choice!="espresso":
            milk_status=check_milk(resources['milk'])
    if water_status and milk_status:
        coffee_status=check_coffee(resources['coffee'])

    if water_status and milk_status and coffee_status:
        print("There are enough resources☕")
        return True
    else:        
        return False

def check_transaction(inserted_money,drink_cost):

    if inserted_money>=drink_cost:
        change = round(inserted_money - drink_cost,2)
        print(f"Here is ${change} in change.")
        global money
        money+=drink_cost
        return True
    else:
        print("Sorry that's not enought money.")
        return False

def brew_caffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is you {drink_name}")

keep_operating="on"
user_choice=""
money=0.0
resources_status= False
payment_status= False


while keep_operating!="off":
    user_choice=input("What would you like? (espresso/latte/cappuccino): ")

    if user_choice=="report":
        print_report(money,resources)
    elif user_choice=="espresso" or user_choice=="latte" or user_choice=="cappuccino":
        resources_status=check_resources(user_choice,resources)
        if resources_status:
            inserted_money=process_coins()
            if check_transaction(inserted_money,MENU[user_choice]['cost']):
                brew_caffee(user_choice,MENU[user_choice]['ingredients'])

     
    elif user_choice=="off":
        keep_operating="off"




