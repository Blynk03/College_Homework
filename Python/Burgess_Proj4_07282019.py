######################################################
# Lavelle Burgess
# Project 4
# 22 Jul 2019
# Version 1.0
######################################################

######################################################
# Description: Write a program that create a class called
# Professors that would contain these attributes: Professor
# Name, Course_ID, Description, and Location. 
######################################################

######################################################
# Variables
######################################################
teacherArray = [] #Holds the teacher objects

######################################################
# Classes
######################################################

class teacherObject:
    name = ""
    ID = ""
    Desc = ""
    Loc = ""
    
    def __init__(self, paramName, paramID, paramDesc, paramLoc): #Constructor for teacherobject
        self.name = paramName
        self.ID = paramID
        self.Desc = paramDesc
        self.Loc = paramLoc

    def showResults(self):
        print(self.name + "        " + self.ID + "        " + self.Desc + "        " + self.Loc)
######################################################
# Functions
######################################################

def addTeacher():
    if(len(teacherArray) <= 5):
        teacherName = input("Please enter the teacher's first and last name: ")
        courseID = input("Please enter the course ID: ")
        courseDesc = input("Please enter the course description: ")
        courseLoc = input("Please enter the course location: ")

        teacherOb = teacherObject(teacherName, courseID, courseDesc, courseLoc)
        teacherOb.showResults
        teacherArray.append(teacherOb)
    else:
        print("There are more than 5 teacher objects created.")
def displayTeachers():
    for i in range(len(teacherArray)):
        teacherArray[i].showResults()

'''x = ""
while (x != "x"):
    x = input("Press 1 to add a new teacher to the list, or press 2 to display teachers, and press 'x' to exit")
    if (x == '1'):
        addTeacher()
    elif (x == '2'):
        print("Professor Name     Course_ID     Description     Location")
        displayTeachers()
    elif (x == 'x'):
        print("Finished adding teachers.")
    else:
        print("This is not a valid option.")'''

'''teacherOb1 = teacherObject("Azhar Ishaque", "3771", "Python", "Hickam AFB")
teacherOb2 = teacherObject("Azhar Ishaque", "3301", "Databases", "Hickam AFB")
teacherOb3 = teacherObject("Hua He", "1123", "Statistics", "Hickam AFB")
teacherOb4 = teacherObject("Azhar Ishaque", "3771", "Python", "Hickam AFB")
teacherOb5 = teacherObject("Azhar Ishaque", "3771", "Python", "Hickam AFB")
teacherOb6 = teacherObject("Azhar Ishaque", "3771", "Python", "Hickam AFB")
teacherArray.append(teacherOb1)
teacherArray.append(teacherOb2)
teacherArray.append(teacherOb3)
teacherArray.append(teacherOb4)
teacherArray.append(teacherOb5)
teacherArray.append(teacherOb6)
displayTeachers()'''

