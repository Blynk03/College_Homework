######################################################
# Lavelle Burgess
# Project 2
# 14 Jul 2019
# Version 1.0
######################################################

######################################################
# Description: Write a Python program that will compute your bill including the tax and tip.
######################################################

######################################################
# Establishing Functions for Computing a bill
######################################################

# This is the main menu that uses if/else statements to allow the user to pick submenues or check out.
# Python does not have switch case to my knowledge, so I used if statements.
def MenuDriver():
    print("Welcome to Delicious Meal Family Restaurant")
    menuSelection = ""
    while menuSelection != "5":
        print("Please select a menu option.")
        print("1: View Food Items.")
        print("2: View Drink Items.")
        print("3: View Order.")
        print("4: Check Out.")
        print("5: Exit Menu.")
        menuSelection = input("Selection: ")

        # Other functions will be called based on user input
        if (menuSelection == "1"):
            print("Viewing Food Items.")
            FoodMenu()
        elif (menuSelection == "2"):
            print("Viewing Drink Items.")
            DrinkMenu()
        elif (menuSelection == "3"):
            print("Viewing Order.")
            ViewOrder()
        elif (menuSelection == "4"):
            print("Checking Out")
            GetTotal()
        elif (menuSelection == "5"):
            print("Exiting Menu")
            exit()
        else:
            print("Invalid Selection, try again.")

# Sub menu for food items, uses AddItem function to build an order for the user
def FoodMenu():
    print("Food Items")
    FoodSelection = ""
    while FoodSelection != "6":
        print()
        print()
        print("1: Battered Squid with White Wine Sauce. $" + stock['Squid'])
        print("2: Stewed Lobster with Rice and Butter Sage Sauce. $" + stock['Lobster'])
        print("3: Warm Gruel with Thick-cut Bacon. $" + stock['Gruel'])
        print("4: Salted Beef with Mushrooms and Water Chestnuts. $" + stock['Beef'])
        print("5: Seared Chicken with Sliced Turnips and Fried Apples. $" + stock['Chicken'])
        print("6: Exit Food Menu.")
        FoodSelection = input("Selection: ")

        if (FoodSelection == "1"):
            print("Adding Squid to the order.")
            AddItem('Squid')
        elif (FoodSelection == "2"):
            print("Adding Lobster to the order.")
            AddItem('Lobster')
        elif (FoodSelection == "3"):
            print("Adding Gruel to the order.")
            AddItem('Gruel')
        elif (FoodSelection == "4"):
            print("Adding Beef to the order.")
            AddItem('Beef')
        elif (FoodSelection == "5"):
            print("Adding Chicken to the order.")
            AddItem('Chicken')
        elif (FoodSelection == "6"):
            print("Exiting Food Menu")
        else:
            print("Invalid Selection, try again.")

# Sub menu for drink items, uses AddItem function to build an order for the user
def DrinkMenu():
    print("Drink Items")
    DrinkSelection = ""
    while DrinkSelection != "6":
        print()
        print()
        print("1: Rich Rose Pear Wine. $" + stock['Pear Wine'])
        print("2: Bubbly White Plum Wine. $" + stock['Plum Wine'])
        print("3: Strong Black Coffee. $" + stock['Coffee'])
        print("4: Bitter Ginger Beer. $" + stock['Ginger Beer'])
        print("5: Oak Cake Stout Beer. $" + stock['Beer'])
        print("6: Exit Drink Menu.")
        DrinkSelection = input("Selection: ")

        if (DrinkSelection == "1"):
            print("Adding Pear Wine to the order.")
            AddItem('Pear Wine')
        elif (DrinkSelection == "2"):
            print("Adding Plum Wine to the order.")
            AddItem('Plum Wine')
        elif (DrinkSelection == "3"):
            print("Adding Coffee to the order.")
            AddItem('Coffee')
        elif (DrinkSelection == "4"):
            print("Adding Ginger Beer to the order.")
            AddItem('Ginger Beer')
        elif (DrinkSelection == "5"):
            print("Adding Stout Beer to the order.")
            AddItem('Beer')
        elif (DrinkSelection == "6"):
            print("Exiting Drink Menu")
        else:
            print("Invalid Selection, try again.")

# This method adds the users selection to the order
def AddItem(paramItemName):
    orderArray.append(paramItemName)

# This will loop through the order array and display its contents and the associated stock dict value for the price.
def ViewOrder():
    if (len(orderArray) == 0):
        print("You have not ordered any items yet.")
    else:
        print()
        print()
        print("Current Order: ")
        for i in range(len(orderArray)):
            print(orderArray[i] + " $" + stock[orderArray[i]])

# GetTotal will loop through the order array and get the sum of all of the prices. It then calls CalculateTotal to apply taxes and tips.
def GetTotal():
    if (len(orderArray) >= 3):
        subTotal = 0.00
        for i in range(len(orderArray)):
            subTotal = float(stock[orderArray[i]]) + subTotal
        CalculateTotal(subTotal)
        exit()
    else:
        print("You must order at least 3 items, you currently have " + str(len(orderArray)))
    
# This will apply sales tax and tips to the subtotal and then calculate the final bill
def CalculateTotal(paramSubTotal):
    ConstSalesTax = .0476
    ConstTipRate = .18
    SalesTax = paramSubTotal * ConstSalesTax
    Tips = (paramSubTotal + SalesTax) * ConstTipRate
    TotalSale = paramSubTotal + SalesTax + Tips

    print()
    print()
    print("Order Bill")
    print("SubTotal: " + '${0:.2f}'.format(paramSubTotal))
    print("Sales Tax: " + '${0:.2f}'.format(SalesTax))
    print("Tip: " + '${0:.2f}'.format(Tips))
    print("Grand Total: " + '${0:.2f}'.format(TotalSale))


# Initializing variables and starting the program through the MenuDriver Function
orderArray = []
stock = {'Squid':'20.35', 'Lobster':'23.99', 'Gruel':'10.99', 'Beef':'19.75', 'Chicken':'17.89', 'Pear Wine':'4.25', 'Plum Wine':'3.79', 'Coffee':'3.00', 'Ginger Beer':'4.05', 'Beer':'3.65'}
MenuDriver()
