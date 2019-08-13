######################################################
# Lavelle Burgess
# Project 5
# 04 Aug 2019
# Version 1.0
######################################################

######################################################
# Description: Write a Python program that asks a user
# to enter score obtained from each of the five class
# projects and calculate the sum of scores.  Each
# project should weigh 20 points to make up 100 points
# for the five projects. Then, add score for all five
# projects to find the grade according to the  total
# score obtained by the student. The letter grade
# should be between A and F.
# Between 90-100 is A, 80-89, B, 70-79 is C, 60-69 D,
# and less than 60  will get F.
######################################################

######################################################
# Variables
######################################################
gradeScores = []

######################################################
# Classes
######################################################

######################################################
# Functions
######################################################
def addGrade(paramNumber):
    if (len(gradeScores) < 5):
        indivGrade = int(input("Enter the grade for assignment " + str(paramNumber) + ": "))
        if indivGrade >20:
            extraCredit = input("Is there extra credit for this assignment? y or n: ")
            if extraCredit == "n":
                indivGrade = 20
            else:
                print("Applying extra credit.")
        else:
            print("")
        gradeScores.append(indivGrade)
    else:
        print("There are already 5 grades in the book")

def displayGrades():
    for i in range(len(gradeScores)):
        print(gradeScores[i])
def calculateFinalScore():
    subtotalScore = 0
    for i in range(len(gradeScores)):
        subtotalScore = subtotalScore + gradeScores[i]
    finalScore = subtotalScore
    return finalScore

def determineGrade(paramScore):
    print(paramScore)
    if paramScore >= 90:
        FinalGrade = "A"
        
    elif paramScore >= 80:
        FinalGrade = "B"
    elif paramScore >= 70:
        FinalGrade = "C"
    elif paramScore >= 60:
        FinalGrade = "D"
    else:
        FinalGrade = "F"
    return FinalGrade
    
######################################################
# Start of Program
######################################################
x = 0
while x <= 4:
    addGrade(x + 1)
    x = x + 1
displayGrades()
final = calculateFinalScore()
print('With a score of ' + str(final) + ' your final grade is an ' + determineGrade(final) + '.')

