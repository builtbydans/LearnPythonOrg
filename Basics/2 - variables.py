# Every variable in Python is an object
myint = 7
print(myint)

# Floating point numbers can be explicitly typed or using the float func()
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

# Strings are defined by single or double quotes
mystring = 'hello'
doublestring = "hello"

# Using double quotes means you can use apostrophes within the string
mystring = "This string will not terminate, don't worry"
print(mystring)

# We can concatenate using different methods in Python
one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

# Assignments to variables can be done simultaneously on one line:
a, b = 3, 4
print(a, b)

# Mixing operators between nums and string is not supported
# This will not work!
one = 1
two = 2
hello = "hello"

print(one + two + hello)

# EXERCISE

# The target of this exercise is to create a string, an integer,
# and a floating point number. The string should be named mystring and
# should contain the word "hello". The floating point number should be named
# myfloat and should contain the number 10.0, and the integer should be named myint
# and should contain the number 20.

mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
