######################################################
# Lavelle Burgess
# Project 1
# 01 Jul 2019
# Version 1.0
######################################################

######################################################
# Description: Write a program that accepts a sentence and calculate the number of letters and digits.
######################################################


# Initializing variables

SampleString = input("Please enter a sentence: ") #"My First Python Program! 125789"
print(SampleString) #Just to confirm that the input was correctly assigned to SampleString
LetterCount = 0
NumberCount = 0

#Using a for loop to split a string into individual characters
for i in range(len(SampleString)): #len() will return a count of the total characters in a string
    #Using comparison operator to determine if a character at position i is a number.
    if SampleString[i].isdigit() == True :
        #increment the count if the character is a number
        NumberCount = NumberCount + 1
    #If a character at position i is not a number, then we can assume it is a character
    else:
        #increment the count if the character is a letter
        LetterCount = LetterCount + 1

#prints out the count for both letters and numbers
print("Letters: " + str(LetterCount))
print("Digits: " + str(NumberCount))


