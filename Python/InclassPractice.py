'''a = [1, 2, 3, 4, 5, [6,4,5]]
print(a[5][1])
print(5+4*2) #python does PEMDOS on its own
print(5//2) #5/2 without the decimal place
print(5/2) #5/2 with decimal place

print(5*2) #5 x 2
print(5**2) #5^2

#List []
#Tuples ()
#Sets {}
#Dict {}
print("Location of a in memory " + str(id(a)))

a = [2, 2, 2, 2, 1, [6,4,5]]
print("Location of a again in memory " + str(id(a)))

b = (1,2)
print("Location of b in memory " + str(id(b)))

b = (4,2)
print("Location of b again in memory " + str(id(b)))
x = ['cats', 'dogs', 8, 'rats', 12]
x[0] = 'lions'
print(x)

y = ('cats', 'dogs', [8, 6, 7], 'rats', 12)
print(y[2][1])
#y[4] = "Something new" #This wont work, tuple

y[2][1] = 7
print(y[2][1])
print(x[1:])
print(x[::2])

f=['apples', 'bananas', 'cherries', 'mangoes', 'grapes']
print(f)
f + ['melon'] #This will not actually add melon to the list
print(f)
f += ['melon']
print(f)
f.append('beetroots')
print(f)
f = f[:-1]
print(f)
del(f[0])
print(f)

s = [1,2,3,6,78,5,4,32,6,543,23,45,89,7,5,34]
print(s)
#s.sort()
print(sorted(s)) #doesn't actually save a sorted s like s.sort() will do
print(s)
print(len(s))
print(s.count(5)) #This is case sensitive

list1 = [2, 3, 4, 5, 6, 7, 8]
print(list1)
list1.pop()
print(list1)
list1.pop(0)
print(list1)
list1.insert(0,1) #insert replaces push for a stack
print(list1)

#3 ways of making a dictionary
d = {'apple': 7.5, 'banana': 6.7, 'carrot': 3.9}
print("The size of an apple is: " + str(d['apple']))
d2 = dict(c=5, d=3.0)
print(d2['d'])
d3 = dict({'e':4, 'g': 3.5})
print(d3)
print(d3['g'])'''

'''
y = int(input("What is y? "))
if y < 0:
    y = 0
    print("Negative number set to 0")
elif y == 0:
    print("Baseline")
elif y == 3771:
    print("Python Course")
else:
    print("Some other course")'''

'''
x = {'a': 10, 'b': 15, 'c': 20}
for m in x.keys():
    print("The key is %s and the value is %d" % (m, x[m])) '''
'''
count = 0
while count < 3:
    print("The count is %d" % count)
    count = count + 1 '''
'''
for ltr in "Python":
    if ltr == 'h':
        continue
    print(ltr)'''
filehandle = open('test.txt', 'w')
txt = "Python\nCSCI 3771\nAzhar Ishaque\naishaque@hpu.edu"
filehandle.write(txt)
filehandle.close()

filehandle = open('test.txt', 'r')
#print(filehandle.read())
print(filehandle.readlines())
filehandle.close()

'''import os
os.rename('test.txt', 'test2.txt')
os.remove('test2.txt')'''
'''import turtle
myTurtle = turtle.Turtle()
wn = turtle.Screen()'''
'''wn.bgcolor('pink')
myTurtle.forward(100)
myTurtle.left(90)
myTurtle.forward(100)
myTurtle.left(90)
myTurtle.forward(100)
myTurtle.left(90)
myTurtle.forward(100)
myTurtle.circle(100)

myTurtle.forward(50)
myTurtle.left(90)
myTurtle.forward(50)
myTurtle.left(90)
myTurtle.forward(50)
myTurtle.left(90)
myTurtle.forward(50)
myTurtle.circle(50)

myTurtle.forward(25)
myTurtle.left(90)
myTurtle.forward(25)
myTurtle.left(90)
myTurtle.forward(25)
myTurtle.left(90)
myTurtle.forward(25)
myTurtle.circle(25)

myTurtle.forward(12)
myTurtle.left(90)
myTurtle.forward(12)
myTurtle.left(90)
myTurtle.forward(12)
myTurtle.left(90)
myTurtle.forward(12)
myTurtle.circle(12)

myTurtle.forward(200)
myTurtle.left(90)
myTurtle.forward(200)
myTurtle.left(90)
myTurtle.forward(200)
myTurtle.left(90)
myTurtle.forward(200)
myTurtle.circle(200)'''

'''x = 1
size = 200
while x < 13:
    newSize = size - (10 * x)
    myTurtle.forward(newSize)
    myTurtle.left(90)
    myTurtle.forward(newSize)
    myTurtle.left(90)
    myTurtle.forward(newSize)
    myTurtle.left(90)
    myTurtle.forward(newSize)
    myTurtle.circle(newSize)
    x = x + 1'''
'''myTurtle.forward(125)
myTurtle.right(145)
myTurtle.forward(125)
myTurtle.right(145)
myTurtle.forward(125)
myTurtle.right(145)
myTurtle.forward(125)
myTurtle.right(145)
myTurtle.forward(125)
myTurtle.right(145)'''

'''from Burgess_Proj4_07282019 import teacherObject 

teacherOb = teacherObject("Azhar Ishaque", "3301", "Databases", "Hickam AFB")
teacherOb.showResults()

# Recursive Test
def facTest(N):
    if N == 0 or N == 1:
        return 1
    else:
        return N * (facTest(N-1))

print(facTest(15))'''

import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #iPv4
checkLink = input("Enter a url: ")
IP = socket.gethostbyname(checkLink)
print(IP)
PORT=80
address=(IP,PORT)
client.connect(address)



