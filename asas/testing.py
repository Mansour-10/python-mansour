# Python Tutorial

print("Hello, World!")

# Python Introduction

# how we can check our python version ?
#  in terminal we can use (py --version) to show our python version 


# Execute Python Syntax
# Python Indentation
   # ture
if 5 > 2:
   print("Five is greater than two!")

   # true
if 5 > 2:
   print("Five is greater than two!") 
if 5 > 2:
   x = "Five is greater than two!"
   print(x)

   # false

"""if 5 > 2:
 print("Five is greater than two!")
     print("Five is greater than two!")"""
 

# Python Variables

a = 5
s = "Hello, World!"
d = "we're going to gym"

print(a)
print(s)
print(d)


# Comments

# we can use (ctrl+/) to write a comment or change our data to comment 
"""we can use (""" """) for making comment few lines in ones"""

# Creating Variables

x = 5
y = "John"
print(x)
print(y)


# example

a = 4       # a is of type int
x = "Sally" # x is now of type str

print(str(a))
print(x)

# int means numbers 
# and str means letters


# Casting

x = str(3)
y = int(3)
z = float(3.9999)

print(x)
print(y)
print(z)


# Get the Type

x = 6
y = "John62"
z = 3.65

print(type(x))
print(type(y))
print(type(z))


# Single or Double Quotes?

x = "John"
print(x)
#double quotes are the same as single quotes:
x = 'John'
print(x)


# Case-Sensitive

a = 4
A = "Sally"

print(a)
print(A)


# Variable Names


myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
my1var2 = "John"


print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(my1var2)


# Camel Case

myVariableName = "John123"

print(myVariableName)


# Pascal Case

MyVariableName = "John456"

print(MyVariableName)

# Snake Case

my_variable_name = "John789"

print(my_variable_name)


# Many Values to Multiple Variables
x, y, z, a = "apple", "Banana", "Cherry", "Orange"

print(x)
print(y)
print(z)
print(a)


# One Value to Multiple Variables

x = y = z = a = "Zafar"
print(x)
print(y)
print(z)
print(a)


# Unpack a Collection

fruits = ["apple", "banana", "cherry", "watermelon"]
x, y, z, a = fruits
print(x)
print(y)
print(z)
print(a)


# Output Variables

a = "Python is awesome"

print(a)



x = "Python"
y = "is"
z = "awesome"
print(x, y, z)


# we can use + also for the same results

x = "Python"
y = " is"
z = " awesome"
print(x + y + z)

# we can't use + in numbers to print all of them in once

x = 5
y = 10
print(x + y)


x = 5
y = "John"
print(x, y)


# Global Variables

a = " and amazing"
x = "awesome"

def py():
   print("Python is " + x + a)

py()

# another example

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


# another example

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


# another example

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


# Python Numbers

x = 1    # int
y = 2.8  # float
z = 1j   # complex


print(type(x))
print(type(y))
print(type(z))


# int

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))


# float

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

# complex

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))



# convert int to float 

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)
print(a)


# Random Number

import random

print(random.randrange(1, 1100))


# Strings - str

print("Hello World!")
print('Hello World!')


a = "Hello Wrold!!!"
print(a)


# Multiline Strings

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(a)


# Strings are Arrays

a = "Hello, World!"
#    0123456789101112
print(a[11])


# Looping Through a String

for x in "banana":
  print(x) 



# String Length

a = "Hello, World!"
print(len(a))

# Check String

a = "The best things in life are free!"

print("free" in a)


# example

a = "The best things in life are free!"
if "free" in a:
  print("Yes, 'free' is present.")


# Check if NOT

a = "The best things in life are free!"
print("expensive" not in a)

# example

a = "The best things in life are free!"
if "expensive" not in a:
  print("No, 'expensive' is NOT present.")



#  slicing 

b = "Hello, World!"
print(b[2:9])

# Slice From the Start


b = "Hello, World!"
print(b[:5])

# Slice To the End

b = "Hello, World!"
print(b[2:])


# Negative Indexing

b = "Hello, World!"
print(b[-5:-2])

# Python - Modify Strings
# Upper Case

a = "Hello, World!"
print(a.upper())

# Lower Case

a = "Hello, World!"
print(a.lower())

# Remove Whitespace

a = "    Hello, World!    "
print(a.strip()) # returns "Hello, World!"

# Replace String

a = "Hello, World!"
print(a.replace("o", "m"))

# Split String

a = "Hello, everyone in, World!"
print(a.split(",")) # returns ['Hello', ' World!']


# String Concatenation


a = "Hello"
b = "World"
c = a + " " + b
print(c)


# String Format

age = 36
a = "My name is John, and I am {}"
print(a.format(age))

# Boolean Values

print(10 > 9)
print(10 == 9)
print(10 < 9)


# example
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


# Evaluate Values and Variables

print(bool("Hello"))
print(bool(15))


# example

x = "Hello"
y = 15 

print(bool(x))
print(bool(y))



# example

print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))


# Some Values are False

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


# Functions can Return a Boolean

def aaa() :
  return True

print(aaa())

# example

def aaa() :
  return True

if aaa():
  print("YES!")
else:
  print("NO!")




# Python Operators

print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)


# Python Lists

mylist = ["apple", "banana", "cherry"]

print(mylist)


# Allow Duplicate

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)


# List Length

thislist = ["apple", "banana", "cherry"]
print(len(thislist))


# List Items - Data Types

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

# type list 

aaaa = ["apple", "banana", "cherry"]
print(type(aaaa))

# The list() Constructor

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


# Access Items list

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# negative

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])



# Range of Indexes list

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])  

# Check if Item Exists

asas = ["apple", "banana", "cherry"]
if "apple" in asas:
  print("Yes, 'apple' is in the asas list")


