#Python has no command for declaring a variable.
name = "Mohamed Rifai"
age = 25

print(name)


#Variables do not need to be declared with any particular type, and can even change type after they have been set.

x = "Raafiya"
x = 19

print(x)


#Casting

#If you want to specify the data type ofa variable, this can be done with casting.

x = str(3)
y = int(3)
z = float(3)

print(x)
print(y)
print(z)

#You can get the data type ofa variable with the type() function.

x = 5
y = "Rifai"

print(type(x))
print(type(y))


#String variables can be declared either by using single or double quotes:

x = 'Mohamed Rifai'
y = "Mohamed Rifai"

print(x)
print(y)


#Case Sensitive
#Variable names are case-sensitive.
#This will create two variables:

a = 4
A = "Rifai"

print(a)
print(A)


#Legal Variable names

myvar = "Rifai"
my_var = "Rifai"
_my_var = "Rifai"
myVar = "Rifai"
MYVAR = "Rifai"
myvar2 = "Rifai"
print(_my_var)


## Assign multiple values

x, y, z = ("Rifai", "Raafiya", 19)
print(x)
print(y)
print(z)


#Output variables

x = "I love python"
print(x)


#In the print() function, you output multiple variables, separated by a comma:
x, y, z = ("Rifai", "Raafiya", 19)
print(x, y, z)
print(x+ y )  #You can also use the + operator to output multiple variables:



#Global Variable

x = "I love you Raafiya"


def myfunc():
    print("Hi my Dear " + x)

myfunc()


# If you use the global keyword, the variable belongs to the global scope:

def myfunc():
    global x
    x = "Raafiyyyyyyyyyyyyya"

myfunc()
print(x)

#To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "Fantastic"
def myfunc():

    global x
    x = "Gorgeous"

myfunc()

print("Raafi is "+ x)


fruits = ['apple', 'banana', 'cherry']
a, b, c = fruits
print(a)


print("Hello", "World" )

#FInd this out
a = 'Hello'
b = 'World'
print(a + b)

#.........
x = 'awesome'
def myfunc():
  x = 'fantastic'
myfunc()
print('Python is ' + x)