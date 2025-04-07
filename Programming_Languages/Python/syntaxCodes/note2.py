# ################### PYTHON FILE ( PART - 2) :- ####################

## This was my code file while i am learning python from W3School. This is basically a notes/refresher

# ##Lambda Function in Python:
# def myFunc(n):
#     return lambda a : a * n

# myDoubler = myFunc(2)
# myTripler = myFunc(3)

# print(myDoubler(11)) 
# print(myTripler(11))


# ##Simple Class and Object:
# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)

# class Student(Person):
#     def __init__(self, fname, lname, roll, sec):
#         Person.__init__(self, fname, lname)
#         self.rollNo = roll
#         self.section = sec

# x = Student("Mike", "Olsen", "21", "A")
# print(x.rollNo)
# print(x.section)
# x.printname()


# ##base and super() __init()__ :   (NOT UNDERSTAND !!!!!)
# class A:
#     def greet(self):
#         print("Hello from A")

# class B(A):
#     def greet(self):
#         super().greet()  # Calls A's greet
#         print("Hello from B")

# class C(A):
#     def greet(self):
#         super().greet()  # Calls A's greet
#         print("Hello from C")

# class D(B, C):
#     def greet(self):
#         super().greet()  # Calls the next class in MRO
#         print("Hello from D")

# d = D()
# d.greet()

# ##Iterator in Python:
# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self

#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x

# myClass = MyNumbers()
# myIter = iter(myClass)

# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))

# ##StopIteration Statement:
# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self

#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration

# myclass = MyNumbers()
# myiter = iter(myclass)

# for x in myiter:
#     print(x)


# ##Try...Except, Finally and Rise:
# x = 45
# try:                                       # try block lets you test a block of code for errors
#     print(x)      
# except NameError:                          #  block lets you handle the error
#     print("Variable x is not defined")
# except:
#     print("Something went wrong")
# else:                                      # executes if no errors were raised
#     print("Nothing went wrong")
# finally:
#     print("The 'try except' is finished")    # finally block, if specified, will be executed regardless if the try block raises an error or not
##Example :--
# a, b = 75, 25
# d = a/b
# print("Quotient: ", d)
# try:
#     a, b = 75, 0
#     d = a/b
#     print(d)   # ZeroDivisionError will occur.
# except:
#     print("Denominator can't be zero.")
    
# try:
#     a = int(input("Enter Numerator :"))
#     b = int(input("Enter Denominator :"))
#     d = a/b
#     print("Quotient: ", d)
#     list = [10, 20, 30, 40, 50]
#     print ("Index 3 has ", list[3])
#     print ("Index 5 has ", list[5])     # IndexError will occur.
# except ZeroDivisionError:
#     print("Denominator can't be zero.")
# except IndexError:
#     print("Index out of bound.")                    # if ZeroDivisionError occurs prnt function for the lists are not executed.


##File Handling in Python:
