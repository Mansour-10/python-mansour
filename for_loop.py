# for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 


# example
fruits = ["10", "20", "30"]
for x in fruits:
  y = x * 2
  print(y)  

# Looping Through a String
for x in "Mansour":
  print(x)  

# The break Statement

list = ["Asma", "Mansour", "Afrahin"]
for x in list:
  print(x)
  if x == "Mansour":
    break
  
# break come before print

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

# The continue Statement

name = ["Asma", "Mansour", "Afrahin"]
for x in name:
  if x == "Mansour":
    continue
  print(x)

# The range() Function

for x in range(10):
  print(x)

for x in range(6):
  print("Mansour")  


for x in range(2, 6):
  print(x)
   

for x in range(2, 30, 4):
  print(x)

# Else in For Loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")

# Else in For Loop break

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")  


# Nested Loops

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

# The pass Statement

for x in [0, 1, 2]:
  pass