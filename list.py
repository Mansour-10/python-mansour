students = ["MAnsour", "Zafar", "Wais", "Shams", "Esmat", "Safa"]
#               0         1       2         3       4        5
print(students)

students = ["MAnsour", "Zafar", "Wais", "Shams", "Esmat", "Safa"]
#length
print(len(students))


students = ["MAnsour", "Zafar", "Wais", "Shams", "Esmat", "Safa"]

print(students[0])


students = ["MAnsour", "Zafar", "Wais", "Shams", "Esmat", "Safa"]

print(students[-1])

students = ["MAnsour", "Zafar", "Wais", "Shams", "Esmat", "Safa"]

print(students[-2])

students = ["MAnsour", "Zafar", "Wais", "Shams", "Esmat", "Safa"]

print(students[0:3])


students = ["MAnsour", "Zafar", "Wais", "Shams", "Esmat", "Safa"]

print(students[:3])

students = ["MAnsour", "Zafar", "Wais", "Shams", "Esmat", "Safa"]

print(students[2:])


students = ["MAnsour", "Zafar", "Wais", "Shams", "Esmat", "Safa"]

print(students[-3:-1])


students = ["MAnsour", "Zafar", "Wais", "Shams", "Esmat", "Safa"]
if"Wais" in students:
   print("Present")


students = ["MAnsour", "Zafar", "Wais", "Shams", "Esmat", "Safa"]
if"Ahmad" in students:
   print("Present")
else:
   print("absent")



#change item value

x = ["Zafar", "Farooq", "ahmad"]
x[2] = "Mansour"
print(x)


x = ["Zafar", "Farooq", "ahmad", "sana", "mosa"]
x [2:4] = ["Mansour", "Shaheer"]
print(x)


#add list items

students = ["MAnsour", "Zafar", "Wais", "Shams", "Esmat", "Safa"]
students.append("Asma")
print(students)


#extend list

first = ["Masnour", "Zafar", "Walid"]
second = ["Asma", "Sana", "Safa"]
first.extend(second)
print(first)

#remove item

students = ["MAnsour", "Zafar", "Wais", "Shams", "Esmat", "Safa"]
students.remove("Shams")
print(students)