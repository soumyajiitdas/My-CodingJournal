##Question 6-1 & 6-7:
person1 = {'first_name': 'morgan', 'last_name':'stark', 'age': 4, 'city': 'new york',}
person2 = {'first_name': 'katherine', 'last_name':'elizabeth', 'age': 22, 'city': 'california',}
person3 = {'first_name': 'kamala', 'last_name':'khan', 'age': 16, 'city': 'new jersey',}

# for key, value in person1.items():
#     print(f"{key}: {value}")

people = [person1, person2, person3]      #for question 6-7
for person in people:
    print(person)


##Question 6-2 & 6-10:
fav_num1 = {'smriti': 18, 'perry': 8, 'ronald': 7, 'leonel': 10, 'sana': 3, }
fav_num2 = {'smriti': [18, 7], 'perry': [8, 9], 'ronald': [7, 3], 'leonel': [10, 5], 'sana': [3, 6], }   #for question 6-10
# for key, value in fav_num1.items():
#     print(f"{key.title()}'s favorite number is {value}.")
for key, value in fav_num2.items():
    print(f"{key.title()}'s favorite numbers are:")
    for num in value:
        print(num)


##Question 6-3 & 6-4:
glossary = {
    "NameError": "It arise for not setting a variable's value before using or made a spelling mistake.",
    "SyntaxError": "The interpreter doesn’t recognize something in the code as valid Python code.",
    "IndexError": "Python can’t find an item at the index that is requested.",
    "IndentationError": "When Python expects an indented block and doesn’t find one or vise versa.",
    "LogicalError": "The syntax is valid Python code, but the code does not produce the desired result.",
    "TypeError": "It arises when an operation or function is applied to an object of an inappropriate datatype.",
}
print("The errors discussed in previous chapters(1st to 5th) and their occurrence cause:")
for key, value in glossary.items():
    print(f"{key}:\n\t{value}")


#Question 6-5:
rivers = {'nile': 'egypt', 'amazon': 'south america', 'ganges': 'india'}
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")


##Question 6-6:
desired_persons = ['tim', 'danny', 'jane', 'edward', 'eric', 'jordan', 'sana',]
favorite_languages = {'jane': 'python','sarah': 'c','edward': 'rust','tim': 'python',}

for person in desired_persons:
    if person in favorite_languages.keys():
        print(f"{person.title()}, thank you for your response.")
    else:
        print(f"{person.title()}, you are invited to take the poll.")


##Question 6-8:
pet_owner1 = {'animal_kind': 'cat', 'owner': 'sarah'}
pet_owner2 = {'animal_kind': 'dog', 'owner': 'edward'}
pet_owner3 = {'animal_kind': 'hamster', 'owner': 'danny'}
pet_owner4 = {'animal_kind': 'rabbit', 'owner': 'jane'}
pet_owner5 = {'animal_kind': 'guinea pig', 'owner': 'eric'}

pets = [pet_owner1, pet_owner2, pet_owner3, pet_owner4, pet_owner5]
for pet in pets:
    print(pet)


##Question 6-9:
favorite_places = {
    'zara': ['goa'],
    'jane': ['ladakh', 'simla'],
    'sana': ['andaman', 'banaras', 'darjeeling'],
}
for name, places in favorite_places.items():
    if len(places) == 1:
        print(f"{name.title()}'s favorite place is:")
    else:
        print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(place.title())


##Question 6-11:
cities = {
    'new york': {
        'country': 'usa',
        'population': 8_623_000,
        'fact': 'The city is known for its iconic skyline.',
    },
    'tokyo': {
        'country': 'japan',
        'population': 9_273_000,
        'fact': 'Tokyo is the capital of Japan.',
    },
    'mumbai': {
        'country': 'india',
        'population': 12_478_000,
        'fact': 'Mumbai is the financial capital of India.',
    },
}
for city, city_info in cities.items():
    print(f"{city.title()}:")
    for key, value in city_info.items():
        print(f"\t{key.title()}: {value}")

##Question 6-12:
# i will do it later...