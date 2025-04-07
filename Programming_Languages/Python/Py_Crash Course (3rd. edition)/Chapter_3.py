## Question 3-1 & 3-2:
my_friends = ['abhijit', 'indra', 'raihan', 'joy', 'puskar', 'azam']

for name in my_friends:
    # print(name)
    print(f"{name.title()} is my good friend.")


## Question 3-3:
cars = ['BMW', 'Audi', "Lamborghini", "Bugatti"]

for car in cars:
    print(f"I would like to own a {car}")


## Question 3-4 to 3-7 and 3-9:
guest_list = ['person1', 'person2', 'person3', 'person4']

for guest in guest_list:
    print(f"{guest}, for my birthday celebration, I would like to invite you for dinner tomorrow at ABC Restaurant.")

print("\nSorry to hear that person3 will not come for tomorrow's dinner for some personal reason.\n")
guest_list[2] = 'person5'
for guest in guest_list:
    print(f"{guest}, for my birthday celebration, I would like to invite you for dinner tomorrow at ABC Restaurant.")

print("\nGuys I have found a bigger table for tomorrow's dinner, now I can invite more friends.\n")
guest_list.insert(0, 'person6')
guest_list.insert(3, 'person7')
guest_list.append('person8')
for guest in guest_list:
    print(f"{guest}, for my birthday celebration, I would like to invite you for dinner tomorrow at ABC Restaurant.")

print(f"Guys! you all {len(guest_list)} are invited for tomorrow's birthday party.")                          # for Question 3-9

print("\nSorry to inform you that I can invite only two people for dinner because new dinner table will not arrive in time for the dinner.\n")
while len(guest_list) > 2:
    popped_guest = guest_list.pop()
    print(f"{popped_guest}, I'm very sorry, I can't invite you for the dinner.")
for guest in guest_list:
    print(f"{guest}, you are still invited for tomorrow's dinner.")

del guest_list[0]                                                           #deletes 1st element with index 0. Remaining 1 element with index 0.
del guest_list[0]                                                           #deletes the last element with index 0.
print("\nAfter deleting, the guest list is ", guest_list)


##Question 3-8:
places_list = ['darjeeling', 'simla', 'agra', 'ladakh', 'andaman']
print(places_list)

print(sorted(places_list))
print(places_list)

print(sorted(places_list, reverse=True))
print(places_list)

places_list.reverse()
print(places_list)

places_list.reverse()
print(places_list)

places_list.sort()
print(places_list)

places_list.sort(reverse=True)
print(places_list)


##Question 3-10:
# I will do it later...