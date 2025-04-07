# ################### PYTHON FILE ( PART - 1) :- ####################

## This was my code file while i am learning python from W3School. This is basically a notes/refresher

# Python indentation - It is the spaces at the beginning of a code line. always should >= 1

# Python comment - starts with #<single line content> or """<multiline content>"""

# Python variables - It is created when a value is assigned to it. str ver is declared using "str" or 'str'
# Assign value to multiple variables:
x, y, z = "orange", "banana", "cherry"  #diff ver
print(x)
print(y)
print(z)
x = y = z = "Apple"    #same ver
print(x)
print(y)
print(z)
# Output of a variable - done by print() function. Use + (not work for str with int) or , to combine multiple variable in print() function
print(x + y)
print(x, y)
x = y = 7
print(x + y)   #performs addition.
# Global Variables - Variables created outside of a function. to create a global var inside of a fn use global keyword
x = "awesome"     #global ver
y = "nice"        #global ver
def my_func():
    x = "fantastic"   #local ver
    global y          #global ver overwritten
    y = "love"
    print("Python is " + x)    #always local ver will print inside a fn
my_func()

print("Python is " + x)    #always global ver will print outside a fn
print("Python is " + y)    #output will be 'Python is love'

# Printing same thing without using loop:
print(10 * "Hello World\n")   #print fn will execute 10 times

# ********** DATATYPE :-**********

"""text type - str (string)
numeric type - int (integer), float (floating point), complex (j is img. part)
sequence type - list, tuple, range (list - ordered, changeable; tuple - ordered, unchangeable.)
# list & tuple allow duplicate values but dict & set don't.
mapping type - dict (dictionary)
set type - set, frozenset
boolean type - bool
binary type - bytes, bytearray, memory_view
none type - NoneType"""

x1 = 33.33
x2 = 3+5j
x3 = ["apple", "banana", "cherry"]
x4 = ("apple", "banana", "cherry")

x5 = range(5)
x6 = {"name": "Soumyajit", "age": "19"}
x7 = {"apple", "banana", "cherry"}
x8 = frozenset({"apple", "banana", "cherry"})
x9 = True
x10 = b'Hello'
x11 = bytearray(5)
x12 = memoryview(bytes(5))
x = None

print(x1)
print(type(x1))
print(x2)
print(type(x2))

print(x3)
print(type(x3))
print(x4)
print(type(x4))
print(x5)
print(type(x5))

print(x6)
print(type(x6))

print(x7)
print(type(x7))
print(x8)
print(type(x8))

print(x9)
print(type(x9))

print(x10)
print(type(x10))
print(x11)
print(type(x11))
print(x12)
print(type(x12))

print(x)
print(type(x))

# ********** STRING MODIFICATION :-**********

S1 = "My name is Soumyajit, and I am a good boy."
for R in S1:
    print(R)
if "is" in S1:
    print("YES")
if "bad" not in S1:
    print("NO")

print(len(S1))
print(S1[0:40:2])
print(S1.lower())
print(S1.upper())
print(S1.replace("o", "a"))
print(S1.split(" "))

# ********** STRING FORMAT :-**********


print("Enter age:")
age = input()
print("Enter height (in cm.):")
height = input()
print("Enter weight (in kg.):")
weight = input()

txt = "You are {1} years old, your height is {0} (in cm.) and weight {2} (in kg.)."
print(txt.format(height, age, weight))

# ********* ESCAPE CHARACTERS :-************

""" \' - Single Quote.
    \\ - Backslash.
    \n - New line.
    \r - Carriage Return.
    \t - tab.
    \b - backspace.
    \f - Form Feed.
    \\ooo - Octal value (single backslash then ooo).
    \\xhh - Hex value (single backslash then xhh). """

# ************** Python Operators :-*************

"""Python divides the operators in the following groups:
1.Arithmetic operators
2.Assignment operators
3.Comparison operators
4.Logical operators
5.Identity operators
6.Membership operators
7.Bitwise operators"""

# 1.Arithmetic Operators :-
"""Arithmetic operators are used with numeric values to perform common mathematical operations."""
x = 10
y = 3

print(x + y)    # Addition.
print(x - y)    # Subtraction.
print(x * y)    # Multiplication.
print(x / y)    # Division.
print(x % y)    # Modulus.The remainder after division.
print(x ** y)   # Exponentiation.
print(x // y)   # Floor division. The Quotient after division.

# 2.Assignment Operators :-
"""Assignment operators are used to assign values to variables."""
x1 = 5
print(x1)
x2 = 5
x2 += 3
print(x2)
x3 = 5
x3 -= 3
print(x3)
x4 = 5
x4 *= 3
print(x4)
x5 = 5
x5 /= 3
print(x5)
x6 = 5
x6 %= 3      # This is the Remainder.
print(x6)
x7 = 5
x7 //= 3      # This is the Quotient.
print(x7)
x8 = 5
x8 **= 3
print(x8)
x9 = 5
x9 &= 3
print(x9)
x10 = 5
x10 |= 3
print(x10)
x11 = 5
x11 ^= 3
print(x11)
x12 = 5
x12 >>= 3
print(x12)
x13 = 5
x13 <<= 3
print(x13)

# 3.Comparison Operators :-
"""Comparison operators are used to compare two values."""
x = 7
y = 10
print(x == y)      # '==' equal.
print(x != y)      # '!=' not equal.
print(x > y)       # '>' grater than.
print(x < y)       # '<' less than.
print(x >= y)      # '>=' grater than or equal to.
print(x <= y)      # '<=' less than or equal to.

# 4.Logical Operators :-
"""Logical operators are used to combine conditional statements."""
x = 8
print(x > 3 and x < 10)      # Returns True if both statements are true.
print(x > 3 or x < 4)        # Returns True if one of the statements is true.
# Reverse the result, returns False if the result is true.
print(not (x > 3 or x < 10))

# 5.Identity Operators :-
"""Identity operators are used to compare the objects."""
a = ["apple", "banana"]
b = ["apple", "banana"]
c = x
"""is operator:-"""
print(a is c)   # returns True because c is the same object as a
# returns False because 'a' is not the same object as b, even if they have the same content
print(a is b)
# to demonstrate the difference between "is" and "==":
print(a == b)   # returns True because 'a' is equal to b.
"""is not operator:-"""
print(a is not c)  # returns False because c is the same object as 'a'.
# returns True because x is not the same object as y, even if they have the same content
print(a is not b)
# to demonstrate the difference between "is not" and "!=":
print(x != y)   # this comparison returns False because x is equal to y.

# 6.Membership Operators :-
"""Membership operators are used to test if a sequence is presented in an object."""
x = ["apple", "banana"]
print("banana" in x)     # 'in' operator.
print("mango" not in x)  # 'not in' operator.

# 7.Bitwise Operators :-
"""Bitwise operators are used to compare (binary) numbers."""

"""& (AND) - Sets each bit to 1 if both bits are 1.
| (OR) - Sets each bit to 1 if one of two bits is 1.
^ (XOR) - Sets each bit to 1 if only one of two bits is 1.
~ (NOT) - Inverts all the bits.
<< (Zero fill left shift) - Shift left by pushing zeros in from the right and let the leftmost bits fall off.
>> (Signed right shift) - Shift right by pushing copies of the leftmost bit in from the left,
and let the rightmost bits fall off."""

# ********** BOOLEAN VALUES :-************

print(10 < 12)
print(10 == 10.0)
C = 100
print(isinstance(C, int))

print("Enter 1st Number:")
A = input()
print("Enter 2nd Number:")
B = input()
if A > B:
    print("A is grater than B")
else:
    print("B is grater than A")

# Some Values are False :-
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# *************** LIST :-***************

list1 = list(("apple", False, "mango", 300,"cherry", 45.3, "mango", 5+2j, True))
print(list1)
print(len(list1))
print(type(list1))

# Access Items :-
print(list1[-3])
print(list1[:])   # by default, it considers 0, list1 length respectively.
print(list1[2:8])
# index 3 to 8 element with a gap one element because of "2".
print(list1[3:8:2])
# first character grater than second one when third one is positive. [F Direction]
print(list1[-8:-3])
# first character lesser than second one when third one is negative. [B Direction]
print(list1[-2:-9:-1])

# Count Element :-
c = list1.count("mango")
print(x)

# Check if Exists :-
if "cherry" in list1:
    print("YES")

# Change Item Value :-
list1[3] = 890
print(list1)
list1[2:8] = ["blackcurrant", "strawberry"]  # cut and paste
print(list1)

# Insert items :-
list1.insert(1, "strawberry")  # adds "strawberry" at index no 1.
print(list1)
list1.append("berry")   # add "berry" at the end of the list.
print(list1)
list2 = ["pineapple", "blackberry", "coconut"]
list1.extend(list2)    # marge list2 to list1
print(list1)

# Remove Item :-
list1.remove("mango")
print(list1)  # removes specific item.
list1.pop(4)  # removes specific index. if not specified it removes last one.
print(list1)
del list1[2]  # removes specific index.
print(list1)
# deletes entire list and shows error because list1 already deleted.
del list1
print(list1)
list1.clear()   # only clears list items.
print(list1)

# Loop Through a List :-
for x in list1:
    print(x)
for i in range(len(list1)):     # alternate method
    print(list1[i])
a = 0                            # alternate method using while loop.
while a < len(list1):
    print(list1[a])
    a = a + 1

# List Comprehension :-
my_list1 = []
for x in list2:         # without list comprehension.
    if "a" in x:          # this syntax is not works if bool datatype is present in list.
        my_list1.append(x)
print(my_list1)
my_list2 = [x for x in list2 if "a" in x]    # with list comprehension.
print(my_list2)
# only allowed others except "mango".
my_list3 = [x for x in list1 if x != "mango"]
print(my_list3)
# Iterable
my_list4 = [x for x in range(10)]
print(my_list4)
# Expression
my_list5 = [x.upper() for x in list2]     # list2 elements in capital letter.
print(my_list5)
my_list6 = ["hi" for x in list2]     # list2 each element replaced by "hi".
print(my_list6)
# only replaces banana to orange.
my_list7 = [x if x != "blackberry" else "orange" for x in list2]
print(my_list7)

# Short list :-
list2.sort()       # sort the list alphanumerically.
print(list2)
list2.sort(reverse=True)      # To sort descending.
print(list2)
this_list = [100, 50, 65, 82, 23]
this_list.sort()
print(this_list)
this_list.sort(reverse=True)    # To sort descending.
print(this_list)
# Case Insensitive Sort :-
this_list2 = ["banana", "Orange", "Kiwi", "cherry"]
this_list2.sort()        # by default short() is case-sensitive.
print(this_list2)
# case-insensitive short using key argument str.lower
this_list2.sort(key=str.lower)
print(this_list2)
# Customize Sort Function :-


def myfunc(n):            # 2 blank lines above and below is needed.
    # list shorted based on how close the number is to 50.
    return abs(n - 50)


this_list3 = [100, 50, 65, 82, 23]
# customize function using keyword argument key = function.
this_list3.sort(key=myfunc)
print(this_list3)
# Reverse Order :-
this_list.reverse()   # reverse the order of an alphanumerical list.
print(this_list)

# Copy lists:-
new_list = list2.copy()
print(new_list)
new_list2 = list(list2)   # alternate method.
print(new_list2)

# Join Lists :-
j_list = list1 + list2
print(j_list)
for x in list2:      # alternate method using append().
    list1.append(x)
print(list1)
list1.extend(list2)    # alternate method using extend().
print(list1)

# *************** TUPLE :-***************

tuple1 = tuple(("dog", "cat", True, "cow", 295.90,
               "elephant", False, "cat", 5+7j, "dog"))
print(tuple1)
# for single element in tuple add a "," at the end otherwise it will not recognise as a tuple:
my_tuple = ("deer",)
print(my_tuple)
print(len(tuple1))
print(type(tuple1))

# Access Items :-
print(tuple1[-4])
print(tuple1[2:-3])
print(tuple1[::-3])

# check if item exists:
if False in tuple1:
    print("YES")
else:
    print("NO")

# Change tuple value:
y = list(tuple1)
y[1] = "goat"
tuple2 = tuple(y)
print(tuple2)
# Add items in tuple:
z = list(tuple1)
z.append("monkey")
tuple3 = tuple(z)
print(tuple3)
# Add tuple to a tuple:
tuple1 += my_tuple
print(tuple1)
# Remove item from tuple:
x = list(tuple1)
x.remove("dog")
xy = tuple(x)
print(xy)
# this will delete the tuple1 tuple and show error because tuple1 already deleted.
del tuple1
print(tuple1)
# joint two tuple:
tuple4 = tuple1 + my_tuple
print(tuple4)
multiply = tuple1 * 2    # Multiply tuple
print(multiply)

# Tuple unpacking:
animals = ("cat", "dog", "goat", "sheep", "fox")
(c, *d, f) = animals
# if variables less than values, add "*" to assign variables at a list.
print(c)
print(d)
print(f)

# Loop tuple:
for x in tuple1:
    print(x)
for i in range(len(tuple1)):   # alternate method.
    print(tuple1[i])           # loop through index numbers.
t = 0
while t < len(tuple1):       # alternate method.
    print(tuple1[t])         # using a while loop.
    t = t+1

# Tuple Methods:
new_tuple1 = tuple1.index(False)     # shows the index no. of False in tuple1.
print(new_tuple1)
# shows the no. of "dog" value present in tuple1.
new_tuple2 = tuple1.count("dog")
print(new_tuple2)

# ******************** SETS :-******************

set1 = {"violet", "indigo", "blue", "green", "yellow",
        "orange", "red", 7j, False, 50.44, "red"}
print(set1)       # Set also written as set((...))
print(len(set1))
print(type(set1))

# Access items:-
for x in set1:    # loop through list.
    print(x)
print("violet" in set1)   # return bool value.

# Add items :-
set1.add("brown")   # set items not changeable only addable.
print(set1)

# Add sets :-
set2 = {"pink", "black", "grey", "white"}
set3 = set1.union(set2)
print(set3)
set1.update(set2)       # Alternate method.
print(set1)
# obj in update() can be tuples, lists, dictionaries etc.
set1.update(tuple1)
print(set1)
set1.update(list1)
# Both union() and update() will exclude any duplicate items.
print(set1)

# Remove items :-
set1.remove("indigo")   # removal of non-existence items will rise an error.
print(set1)
set1.discard("indigo")  # Alternate method.
print(set1)            # removal of non-existence items will not rise an error.
x = set1.pop()
print(x)
print(set1)    # only removes last item.
set1.clear()
print(set1)    # return empty set.
del set1
# delete entire set and shows error because dict1 already deleted.
print(set1)

# Set Operations :-
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)       # keep only duplicates.
print(x)
z1 = x.intersection(y)     # alternate method.
print(z1)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)        # keep only the duplicates.
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}       # alternate method.
z2 = x.symmetric_difference(y)
print(z2)

x3 = {"cat", "cow", "dog", "fly", "bee", "bat", "bull"}
y3 = {"crow", "rat", "cow", "bat", "bull", "hen", "fly"}
x3.difference_update(y3)      # set subtraction.
print(x3)

x3 = {"cat", "cow", "dog", "fly", "bee", "bat", "bull"}
y3 = {"crow", "rat", "cow", "bat", "bull", "hen", "fly"}
z3 = x3.difference(y3)     # alternate method.
print(z3)

x3 = {"cat", "dog", "bee", "hen", "bull"}
y3 = {"crow", "rat", "fly", "cow"}
# Returns true if they don't have any common items(i.e. they are disjoint).
z4 = x3.isdisjoint(y3)
print(z4)

x4 = {"bus", "taxi", "bike", "cycle", "boat", "ship", "jet ski"}
y4 = {"ship", "boat", "jet ski"}
# Returns whether another set contains this set or not.
z5 = y4.issubset(x4)
print(z5)
# Returns whether this set contains another set or not.
z6 = x4.issuperset(y4)
print(z6)

# *************** DICTIONARY :-*****************

dict1 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "color": "yellow"
}
print(dict1)
print(len(dict1))
print(type(dict1))

# Access items :-
print(dict1["model"])
x = dict1["model"]   # alternate method.
print(x)
y = dict1.get("model")    # alternate method.
print(y)
z = dict1.setdefault("brand", "BMW")     # returns the value of "brand".
print(z)                                 # if value not exists returns "BMW".

# Get Keys :-
x = dict1.keys()
print(x)
dict1["owner"] = "Scout"   # add new key.
print(x)
print(dict1)

# Get Values :-
x = dict1.values()
print(x)                   # returns only values.
dict1["owner"] = "Scout"   # add new value.
print(x)
print(dict1)             # dictionary after adding new value.
dict1["year"] = 2020     # change a value. This will overwrite previous.
print(dict1)

# Get Items :-
x = dict1.items()
print(x)
dict1["year"] = 2020   # change item.
print(x)
dict1["owner"] = "Scout"    # add item.
print(x)

# Update Dictionary (Add & Change) :-
dict1.update({"owner": "scout"})
print(dict1)                      # Update by adding new.
dict1.update({"year": 2020})
print(dict1)                      # Update by changing.

# Remove Items :-
dict1.pop("model")
print(dict1)      # removes the item with the specified key name.
dict1.popitem()
print(dict1)          # removes the last inserted item.
dict1.clear()         # empties the dictionary.
print(dict1)
del dict1["brand"]    # Remove items using del key.
print(dict1)
del dict1             # delete entire dictionary.
print(dict1)          # shows error.

# Check if Key Exists :-
if "model" in dict1:
    print("YES, IT DOES.")
else:
    print("NO, IT DOESN'T.")

# Loop Through a Dictionary :-
for x in dict1:
    print(x)                  # print only key names one by one.
for x in dict1:
    print(dict1[x])           # print only values one by one.
for x in dict1.values():
    print(x)                  # alternate method.
for x in dict1.keys():
    print(x)                  # alternate method.
for x, y in dict1.items():
    print(x, y)               # loop through keys & values.

# Copy a Dictionary :-
mydict = dict1.copy()
print(mydict)              # copy using copy() method.
mydict = dict(dict1)
print(mydict)              # copy using dict() method.

# Nested Dictionaries :-
family1 = {                   # a dictionary that contains three dictionaries.
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
print(family1)
child1 = {              # Alternate Method.
    # Create three dictionaries, then create one dictionary containing other three dictionaries.
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}

family2 = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
print(family2)

# Other Methods :-
x = ('breakfast', 'lunch', 'dinner')
y = 'done'
this_dict = dict.fromkeys(x, y)
print(this_dict)
