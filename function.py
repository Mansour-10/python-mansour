def multiply():
    x = 24
    y = 365
    print(x * y)

multiply()

def adds():
    x = 260
    y = 940
    print(x + y)

adds()

def divide():
    x = 3500
    y = 15
    print(x / y)

divide()  

def min():
    x = 111
    y = 23
    print(x - y)

min()

# HW 06

def multiply():
    x = 100
    y = 365
    print(x * y)

multiply()

def adds():
    x = 786
    y = 623
    print(x + y)
 
adds()

def divide():
    x = 365
    y = 7
    print(x / y)

divide()  

def min():
    x = 2023
    y = 1997
    print(x - y)

min()




# new lessons for friday 28/07/2023

# Arbitrary Arguments, *args ;

def my_function(*Cars):
  print("best company cars " + Cars[1])

my_function("Toyota", "RangeRover", "Bmw")


# Keyword Arguments ;

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Mansour", child2 = "Shaheer", child3 = "Lima")


def my_function(country, province, city):
  print("i am from " + country, "my province and city is " + province, city)

my_function(country = "afghanistan", province = "Kabul", city = "Shahr-e-naw")


# Arbitrary Keyword Arguments, **kwargs ;

def my_function(**student):
  print("His last name is " + student["lastname"])

my_function(firstname = "Mansour", lastname = "Gulzad")


#  Default Parameter Value ;

def my_function(country = "afghanistan"):
  print("I am from " + country)

my_function("Turkey")
my_function()
my_function("Canada")


# example ;
def my_function(friends = "Zafar"):
  print(friends + " is my friend")

my_function("ahmad ramin")
my_function()
my_function("Jawid")


# Passing a List as an Argument ;

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)


# Return Values ;

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


# The pass Statement

def myfunction():
  pass  
# it will pass the function