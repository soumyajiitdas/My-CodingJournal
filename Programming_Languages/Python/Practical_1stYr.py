##Random problems and code, when i was my 1st year i wrote these...
# 00######## Addition Calculator :-#############
"""print("enter first number:")
x = input()
print("enter second number:")
y = input()
print("sum of the two numbers =", 5 * str(int(x)+int(y)))

# 01##########Square root of a number:##########
print("Enter number:")
num = float(input())
num_sqrt = num**.5
print("the sq. root of %0.3f is: %0.3f " % (num, num_sqrt))
# %0.3f means a floating point with max 3 steps after point(".") eg,- 0.004, 9.001

# 02##########Area of a triangle:##########
print("Enter the sides of a triangle:")
A = float(input())
B = float(input())
C = float(input())
S = (A+B+C)/2
Area = (S*(S-A)*(S-B)*(S-C))**.5
print(" The triangle with sides a = {0}, b = {1}, c = {2} has area {3} sq.units ".format(A, B, C, Area))

# 03##########Solve Quadratic Equation:##########
print("Enter the Coefficient of x^2, x and constant term (all with sign):")
a = int(input())
b = int(input())
c = int(input())
D = (b**2 - 4*a*c)
x1 = (-b+D**.5)/(2*a)
x2 = (-b-D**.5)/(2*a)
print("values of x for equation ({0})x^2 + ({1})x + ({2}) = 0 are:".format(a, b, c))
print(x1, "and", x2)

# 04##########Convert value from Fahrenheit to Celsius:##########
print("Enter the value of Fahrenheit:")
f = float(input())
c = 5*(f-32)/9
print("The value of %0.2f℉ in Celsius scale is %0.2f℃ " % (f, c))

# 05##########Check if a number is ODD or EVEN:##########
print("Enter a Number:")
y = int(input())
if y % 2 == 0:
    print("{} is a EVEN number.".format(y))
else:
    print("{} is a ODD number.".format(y))

# 06##########Check if a Year is a LeapYear or not:###########
print("Enter the Year:")
y = int(input())
if y % 4 or y % 100 or y % 400:
    print("{} is a LeapYear.".format(y))
else:
    print("{} is not a LeapYear.".format(y))

# 07##########Find the Largest among Three numbers:##########
print("Enter three numbers:")
a = int(input())
b = int(input())
c = int(input())
if a >= b and a >= c:
    lar = a
elif b >= a and b >= c:
    lar = b
else:
    lar = c
print("The largest number among {0}, {1} and {2} is {3}.".format(a, b, c, lar))

# 08##########Check if a number is a Prime Number or not:##########
x = int(input("Enter a Number: "))
if x > 1:
    for y in range(2, (x//2)+1):   # instead of (x//2)+1 also written x.
        if (x % y) == 0:
            print(x, "is not a Prime Number.")
            print(y, "times", x//y, "is", x, ".")
            break
    else:
        print(x, "is a Prime Number")
else:
    print(x, "is neither a Prime Number nor composite.")

# 09##########Determination of Plank's Constant from Reading:############
a = float(input("Enter 1st Stopping Voltage (in V unit): "))
b = float(input("Enter 2nd Stopping Voltage (in V unit): "))
if a > b:
    d1 = (a-b)
else:
    d1 = (b-a)
print("Difference of voltages is: ", d1, "V")
x = float(input("Enter 1st frequency (x10¹⁴ sec⁻¹): "))
y = float(input("Enter 2nd frequency (x10¹⁴ sec⁻¹): "))
if x > y:
    d2 = (x-y)
else:
    d2 = (y-x)
print("Difference of frequency is : ", d2, "x10¹⁴ sec⁻¹")
print("Plank's constant(h1) is:")
h1 = (d1/d2)*1.602
print(h1, "x10⁻³³ Joules sec.")
# phase2
p = float(input("Enter Stopping Voltage (in V unit, without sign): "))
q = float(input("Enter Stopping Voltage (in V unit, without sign): "))
if p > q:
    d3 = (p-q)
else:
    d3 = (q-p)
print("Difference of voltages is: ", d3, "V")
r = float(input("Enter frequency (x10¹⁴ sec⁻¹): "))
s = float(input("Enter frequency (x10¹⁴ sec⁻¹): "))
if r > s:
    d4 = (r-s)
else:
    d4 = (s-r)
print("Difference of frequency is : ", d3, "x10¹⁴ sec⁻¹")
print("Plank's constant (h2) is:")
h2 = (d3/d4)*1.602
print(h2, "x10⁻³³ Joules sec.")
# sum
print("Average Planks Constant (h1+h2)/2 = ", (h1+h2)/2, "x10⁻³³ Joules sec.")

# 10##########Determination of Dielectric Constant from Reading:############
c = float(input(print("Entre Capacitance (pf) :")))
e = c / 29.9
print("Dielectric Constant = ", e, "* 100")

# 11##########Determination of Wavelength 0f light from Reading:############
# Phase 1
a = float(input(print("Enter Main Scale Reading (Left Side) (mm): ")))
b = float(input(print("Enter Circular Scale Reading (Left Side) (mm): ")))
t1 = a+b*0.01
print("Total = ", t1, "mm")

c = float(input(print("Enter Main Scale Reading (Right Side) (mm): ")))
d = float(input(print("Enter Circular Scale Reading (Right Side) (mm): ")))
t2 = c+d*0.01
print("Total = ", t2, "mm")

if t1 > t2:
    x = t1-t2
else:
    x = t2-t1
print("Diameter of the Circle (Dm): ", x, "mm")
print("Square of Diameter of the Circle (D²m): ", x**2, "mm²")"""

# Phase 2
# p = float(input((print("Entre the value of D²m+n :"))))
# q = float(input((print("Entre the value of D²m :"))))
# x = p-q
# print("The Difference of the Square of Diameters of the Circles = ", x)
# r = float(input(print("Entre the value of m+n")))
# s = float(input(print("Entre the value of m")))
# y = r-s
# z = x/(4*990*y)
# print("The Wavelength of the light (when R = 0.99m) = ", z, "x10⁻⁷Å")
