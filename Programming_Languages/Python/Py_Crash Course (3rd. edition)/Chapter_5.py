##Question 5-2:
car = 'Bugatti'
print(car == 'BMW')
print(car == 'Bugatti')

print(car != 'Audi')
print(car != 'Bugatti')

print(car.lower() == 'bugatti')
print(car.lower() == 'lamborghini')

num1 = 10
print(num1 == 5)
print(num1 == 10)

print(num1 != 14)
print(num1 != 10)

print(num1 > 7)
print(num1 > 11)

print(num1 < 12)
print(num1 < 8)

print(num1 >= 15)
print(num1 >= 6)

print(num1 <= 10)
print(num1 <= 9)

num2 = 23
print("and keyword condition tests:")
print(num1 <= 10 and num2 >= 23)     #True-True case
print(num1 <= 18 and num2 <= 19)     #True-False case
print(num1 >= 16 and num2 >= 15)     #False-True case
print(num1 <= 7 and num2 <= 21)      #False-False case
##conclusion - if one value is false then it returns false.

print("or keyword condition tests:")
print(num1 <= 10 or num2 >= 23)     #True-True case
print(num1 <= 18 or num2 <= 19)     #True-False case
print(num1 >= 16 or num2 >= 15)     #False-True case
print(num1 <= 7 or num2 <= 21)      #False-False case
##conclusion - if one value is true then it returns true.

print("Checking if a value in a list or not:")
animals = ['dog', 'cow', 'cat', 'fox']
print('fox' in animals)
print('ox' in animals)
print('goat' not in animals)
print('cow' not in animals)


#Question 5-3:
alien_color0 = 'green'
alien_color1 = 'yellow'
if alien_color0 == 'green':           #version 1
    print("You just earn 5 points.")

if alien_color1 == 'green':           #version 2
    print("You just earn 5 points.")

#Question 5-4:
if alien_color0 == 'green':           #version 1
    print("You just earn 5 points.")
else:
    print("You just earn 10 points.")

if alien_color1 == 'green':           #version 2
    print("You just earn 5 points.")
else:
    print("You just earn 10 points.")

#Question 5-5:
alien_color2 = 'red'
if alien_color0 == 'green':             #version 1
    print("You just earn 5 points.")
elif alien_color0 == 'yellow':
    print("You just earn 10 points.")
else:
    print("You just earn 15 points.")

if alien_color1 == 'green':             #version 2
    print("You just earn 5 points.")
elif alien_color1 == 'yellow':
    print("You just earn 10 points.")
else:
    print("You just earn 15 points.")

if alien_color2 == 'green':             #version 3
    print("You just earn 5 points.")
elif alien_color2 == 'yellow':
    print("You just earn 10 points.")
else:
    print("You just earn 15 points.")

##Question 5-6:
age = 20
if age < 2:
    print("The person is a baby.")
elif 2 <= age < 4:
    print("The person is a toddler.")
elif 4 <= age < 13:
    print("The person is a kid.")
elif 13 <= age < 20:
    print("The person is a teenager.")
elif 20 <= age < 65:
    print("The person is a adult.")
else:
    print("The person is a elder.")

##Question 5-7:
fruits = ['mango', 'banana', 'apple', 'grapes', 'guava', 'cucumber']
print(fruits)
favorite_fruits = ['mango', 'apple', 'cucumber']
if 'mango' in favorite_fruits:
    print("I really like mangoes!")
if 'banana' in favorite_fruits:
    print("I really like bananas!")
if 'apple' in favorite_fruits:
    print("I really like apples!")
if 'grapes' in favorite_fruits:
    print("I really like grapes!")
if 'guava' in favorite_fruits:
    print("I really like guavas!")
if 'cucumber' in favorite_fruits:
    print("I really like cucumbers!")

##Question 5-8 & 5-9:
userNames = ['admin', 'eric', 'danny', 'tom', 'jordan', 'sana']
# while userNames:
#     userNames.pop()
if len(userNames) == 0:
    print("We need to find some users!")
for user in userNames:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, thank you for logging in again.")

##Question 5-10:
current_users = userNames[:]
current_users_lower = [user.lower() for user in current_users]
new_users = ['tim', 'Danny', 'jane', 'ben', 'ERIC']
new_users_lower = [user.lower() for user in new_users]
for user in new_users_lower :
    if user in current_users_lower:
        print("You will need to enter a new user name.")
    else:
        print("This user name is available.")

##Question 5-11:
num_list = [num for num in range(1, 10)]
print("Ordinal Numbers:")
for num in num_list:
    if num == 1:
        print("1st")
    elif num == 2:
        print("2nd")
    elif num == 3:
        print("3rd")
    else:
        print(f"{num}th")