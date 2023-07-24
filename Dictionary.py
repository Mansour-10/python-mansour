# dictionary
car = {
    "brand": "LandRover",
    "model": "RangeRover",
    "year": 1997,
}

print(car)

# example 
Deatils = {
    "Name": "Mohammad Mansour",
    "Phone": "+992 777115451",
    "Country": "Afghanistan",
    "LastName": "gulzad",
    "Mail": "gulzad.mansour2018@gmail.com",
    "address": "Vahdat-Dushanbe-Tajikistan",
}

print(Deatils)




# dictionary items
car = {
    "brand": "LandRover",
    "model": "RangeRover",
    "year": 1997,
}

print(car["model"])


# example 
Deatils = {
    "name": "Mohammad Mansour",
    "phone": "+992 777115451",
    "country": "Afghanistan",
    "lastName": "gulzad",
    "mail": "gulzad.mansour2018@gmail.com",
    "address": "Vahdat-Dushanbe-Tajikistan",
}

print(Deatils["address"])


# Duplicates Not Allowed

sos = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020, #it is always chose the last value if it was duplicate
}
print(sos)


# Dictionary Length

sos = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "lastyear": 2020,
}
print(len(sos))


# Dictionary Items - Data Types

x = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(x)

# The dict() Constructor

lists = dict(name = "John", age = 36, country = "Norway")

print(lists) 


# 
