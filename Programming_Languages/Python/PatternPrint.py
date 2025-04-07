###STAR PATTERN PRINTING###
n = 5    #rows number
##BASIC PATTERN 1:-Square(■):
for i in range(n):             #outer loop for no. of rows
    for j in range(n):         #inner loop for no. of columns 
        print("*", end=" ")    #end is used to print stars in one line
    print()                    #it is user to start from next line

print()

##BASIC PATTERN 2:-Right Triangle(◣):
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()

print()

##BASIC PATTERN 3:-Inverted Right Triangle(◤):
for i in range(n):
    for j in range(i, n):
        print("*", end=" ")
    print()

print()

##Applications:-
#1.Mirrored Right Triangle(◢):         (inv. space pattern + mirrored star pattern)
for i in range(n):
    for j in range(i, n):      #dec. pattern of Space
        print(" ", end=" ")
    for k in range(i+1):       #inc. pattern of Star.
        print("*", end=" ")
    print()

print()

#2.Inverted Mirrored Right Triangle Pattern(◥):        (right triangle space pattern + inv. mirrored star pattern)
for i in range(n):
    for j in range(i+1):      #inc. pattern of Space
        print(" ", end=" ")
    for k in range(i, n):     #dec. pattern of Star.
        print("*", end=" ")
    print()

print()

#3.Pyramid Pattern(▲):             (inv. right triangle space pattern + mirrored right triangle star pattern + right triangle star pattern)
for i in range(n):
    for j in range(i, n):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    for l in range(i+1):
        print("*", end=" ")
    print()

print()

#4.Inverted Pyramid Pattern(▼):     (right triangle space pattern + inv. mirrored right triangle star pattern + inv. right triangle star pattern)
for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")
    for k in range(i, n-1):
        print("*", end=" ")
    for l in range(i, n):
        print("*", end=" ")
    print()

print()

#5.Hourglass Pattern:          (inv. pyramid star pattern + pyramid star pattern in the next line)
for i in range(n-1):
    for j in range(i+1):
        print(" ", end=" ")
    for k in range(i, n-1):
        print("*", end=" ")
    for l in range(i, n):
        print("*", end=" ")
    print()
for i in range(n):
    for j in range(i, n):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    for l in range(i+1):
        print("*", end=" ")
    print()

print()

#6. Diamond Pattern(◆):        (pyramid star pattern + inverted pyramid star pattern in the next line)
for i in range(n-1):
    for j in range(i, n):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    for l in range(i+1):
        print("*", end=" ")
    print()
for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")
    for k in range(i, n-1):
        print("*", end=" ")
    for l in range(i, n):
        print("*", end=" ")
    print()

print()

#7.Half Diamond Pattern(▶):            (right triangle star pattern + inv. right triangle star pattern in the next line)
for i in range(n-1):
    for j in range(i+1):
        print("*", end=" ")
    print()
for i in range(n):
    for k in range(i, n):
        print("*", end=" ")
    print()

print()

#8.Inverted Half Diamond Pattern(◀):    (mirrored right triangle + inv. mirrored right triangle in the next line)
for i in range(n-1):
    for j in range(i, n):
        print(" ", end=" ")
    for k in range(i+1):
        print("*", end=" ")
    print()
for i in range(n):
    for j in range(i+1):      
        print(" ", end=" ")
    for k in range(i, n):     
        print("*", end=" ")
    print()

print()

#9.Right Arrow Pattern:       (inv. mirrored right triangle star pattern + mirrored right triangle star pattern)
for i in range(n-1):
    for j in range(i+1):
        print(" ", end=" ")
    for k in range(i, n):
        print("*", end=" ")
    print()
for i in range(n):
    for j in range(i, n):
        print(" ", end=" ")
    for k in range(i+1):
        print("*", end=" ")
    print()

print()

#10.Left Arrow Pattern:      (inv. right triangle star pattern + right triangle star pattern)
for i in range(n-1):
    for j in range(i, n):
        print("*", end=" ")
    print()
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()
