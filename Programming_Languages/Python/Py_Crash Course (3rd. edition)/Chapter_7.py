##Question 7-1:
car = input("What kind of rental car would you like? ")
print(f"Let me see if I can find you a {car}.")


##Question 7-2:
people = input("How many people are in your dinner group? ")
people = int(people)
if people > 8:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready.")


##Question 7-3:
number = input("Enter a number: ")
number = int(number)
if number % 10 == 0:
    print("The number is a multiple of 10.")
else:
    print("The number is not a multiple of 10.")


##Question 7-4 & 7-6:
while True:
    topping = input("Enter a topping for your pizza (or enter 'q' to quit): ")
    if topping.lower() == 'q':
        break
    else:
        print(f"Adding {topping} to your pizza.")


active = True         # for question 7-6
while active:         # different version of above code which use a active variable
    topping = input("Enter a topping for your pizza (or enter 'q' to quit): ")
    if topping.lower() == 'q':
        active = False
    else:
        print(f"Adding {topping} to your pizza.")


##Question 7-5:
while True:
    age = input("Enter your age (or enter 'q' to quit): ")
    if age == 'q':
        break
    age = int(age)
    if age < 3:
        print("For you, the ticket is free.")
    elif 3 <= age <= 12:
        print("For you, the ticket prise is $10.")
    else:
        print("For you, the ticket prise is $15.")


##Question 7-7:
#while True:
    #print("Hello World!")


##Question 7-8:
sandwich_orders = ['grilled cheese', 'pinwheel', 'pastrami', 'veggie', 'cuban', 'pastrami', 'italian', 'tuna', 'pastrami',]
finish_sandwiches = []
print("Deli has run out of Pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    current_order = sandwich_orders.pop()
    print(f"I made your {current_order.title()} sandwich.")
    finish_sandwiches.append(current_order)

print("Sandwich orders made:")
for order in finish_sandwiches:
    print(order.title(), " sandwich")

############ Need to Review this Code ################
# ##Question 7-9:
# # Write a program that polls users about their dream vacation. Write a prompt similar to If you could visit one place in the world, where would you go? Include a block of code that prints the results of the poll.
# dream_vacation = {}
# polling_active = True
# while polling_active:
#     name = input("Enter your name: ")
#     place = input("If you could visit one place in the world, where would you go? ")
#     dream_vacation[name] = place
#     repeat = input("Would you like to let another person respond? (yes/no) ")
#     if repeat.lower() == 'no':
#         polling_active = False