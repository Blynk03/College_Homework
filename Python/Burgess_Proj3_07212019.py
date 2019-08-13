######################################################
# Lavelle Burgess
# Project 3
# 15 Jul 2019
# Version 1.0
######################################################

######################################################
# Description: Write a program in Python 3.x that asks the user to input up to 10 numbers with two decimals into a list.
# The program should calculate and display the min, max, average and sum of the values entered.
# The output should include two decimals for the calculated values. Allow the user to reenter new numbers for calculation.
######################################################

######################################################
# Functions
######################################################
def getMin():
    #returns the smallest number in an array
    if isEmpty() == False:
        return '{0:.2f}'.format(min(numberArray))
    else:
        return "List is empty"
def getMax():
    #returns the highest number in an array
    if isEmpty() == False:
        return '{0:.2f}'.format(max(numberArray))
    else:
        return "List is empty"

def getAverage():
    #returns the average an array
    if isEmpty() == False:
        numberAverage = 0
        numberAverage = float(float(getSum() / len(numberArray)))
        return '{0:.2f}'.format(numberAverage)
    else:
        return "List is empty"

def getSum():
    #returns the sum of an array
    if isEmpty() == False:
        numberSum = 0
        for i in range(len(numberArray)):
            numberSum = numberArray[i] + numberSum
        return float('{0:.2f}'.format(numberSum))
    else:
        return "List is empty"

def displayNumbers():
    # displays the contents of any array
    if isEmpty() == False:
        print("Current Numbers: ")
        for i in range(len(numberArray)):
            print('{0:.2f}'.format(numberArray[i]))

def addNumber(newNumber):
    # appends a value to the array if array is less than 10 numbers
    if len(numberArray) < 10:
 
        if str(newNumber).isalpha() == True:
            print("This is not a number")
        else:
            numberArray.append(float(newNumber))
    else:
        print("The array has reached it's max size")
    
def isEmpty():
    if len(numberArray) == 0:
        print("Operation cancelled, there are no numbers to use")
        return True
    else:
        return False
    
def clearNumbers():
    print("Starting over")
    numberArray.clear()

def MainDriver():
    # This is the start of the program and will ask the user to enter a number or enter x to quit
    print("Select an option, or enter x to exit")
    menuSelection = ""
    while menuSelection != "x" :
        print("1: Add a value to array.")
        print("2: Display the smallest number.")
        print("3: Display the largest number.")
        print("4: Display the sum of all numbers.")
        print("5: Display the average of all numbers.")
        print("6: Display all of the numbers")
        print("7: Start Over")
        menuSelection = input("Selection: ")

        # Other functions will be called based on user input
        if (menuSelection == "1"):
            addNumber(input("Please enter a number: "))
        elif (menuSelection == "2"):
            print("Calculating Min: ")
            print(getMin())
        elif (menuSelection == "3"):
            print("Calculating Max: ")
            print(getMax())
        elif (menuSelection == "4"):
            print("Calculating Sum: ")
            print(getSum())
        elif (menuSelection == "5"):
            print("Calculating Average: ")
            print(getAverage())
        elif (menuSelection == "6"):
            displayNumbers()
        elif (menuSelection == "7"):
            clearNumbers()
        elif (menuSelection == "x"):
            exit()
        else:
            print("Invalid Selection, try again.")
        print("\n\n\n")

######################################################
# Variables
######################################################
#numberArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numberArray = []

######################################################
# Start of Program
######################################################
MainDriver()


