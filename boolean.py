x = 50
z = 7

if x < z:
  print("z is greater than x")
else:
  print("z is not greater than x")


print(bool("welcome"))
print(bool())
print(bool(5456))
print(bool(0))


a = 10
b = 20 
c = 30

if a < b and b < c:
    print("1st you are right!")


a = 10
b = 20 
c = 30

if a < b and b > c:
    print("1st you are right!")

a = 10
b = 20 
c = 30

if a < b or b > c:
    print("2nd you are right!")    



x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

x = ["Mansour", "Zafar"]

print("Mansour" in x)

# returns True because a sequence with the value "banana" is in the list

x = ["Ahmad", "Farooq", "Shams"]

print("Masnsour" not in x)

# returns True because a sequence with the value "pineapple" is not in the list

