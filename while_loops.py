# while loop
i = 1

while i < 9:
  print(i)
  i += 1

# break Statement
a = 1
while a < 9:
  print(a)
  if a == 5:
    break
  a += 1


# continue Statement

i = 0
while i < 8:
  i += 1
  if i == 4:
    continue
  print(i)

# else statement
i = 1
while i < 10:
  print(i)
  i += 1
else:
  print("i is no longer less than 10")  

