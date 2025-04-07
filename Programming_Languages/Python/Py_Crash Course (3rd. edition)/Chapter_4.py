##Question 4-1 & 4-11:
my_pizzas = ['pepperoni', 'veggie', 'cheese', 'chicken onion']

for pizza in my_pizzas:
    # print(pizza.title())
    print(f"I like {pizza.title()} pizza.")
print("I really enjoy pizza with my friends and family while watching movies.\n")

friend_pizzas = my_pizzas[:]                  #for question 4-11
my_pizzas.append('BBQ chicken')
friend_pizzas.append('margherita')
print("\nMy favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza.title())
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())


##Question 4-2:
pet_animals = ['cat', 'dog', 'rabbit']

for pet in pet_animals:
    # print(pet.title())
    print(f" A {pet} would make a great pet.")
print("Any of these animals would make a great pet!\n")


##Question 4-3:
for i in range(1, 21):
    print(i)


#Question 4-4 & 4-5:
one_million = []
for i in range(1, 10_00_001):
    one_million.append(i)
# print(one_million)

print(min(one_million))
print(max(one_million))
print(sum(one_million))


##Question 4-6:
odd_numbers = []
for i in range(1, 21, 2):
    odd_numbers.append(i)
for num in odd_numbers:
    print(num)


##Question 4-7:
multiple_3 = []
for i in range(1,11):
    multiple_3.append(i*3)
for num in multiple_3:
    print(num)


##Question 4-8 to 4-10:
cubes = [i**3 for i in range(1,11)]   #list comprehensions
for cube in cubes:
    print(cube)

print("\nThe first three items in the cubes list are:")    ##for question 4-10
for cube in cubes[:3]:
    print(cube)

print("The three items from the middle of the cubes list are:")
for cube in cubes[3:6]:
    print(cube)

print("The last three items in the cubes list are:")
for cube in cubes[-3:]:
    print(cube)


##Question 4-12:
# I will do it later...


##Question 4-13:
food_tuple = ('veg rice', 'egg rice', 'fish rice', 'chicken biryani', 'mutton biryani')
for food in food_tuple:
    print(food.title())

#food_tuple[1] = 'roti tadka'

food_tuple = ('veg rice', 'roti tadka', 'fish rice', 'chicken egg biryani', 'mutton egg biryani')
print("\nUpdated food list:")
for food in food_tuple:
    print(food.title())