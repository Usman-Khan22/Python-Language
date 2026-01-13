# BUILT-IN FUNCTIONS:
# these are the predefined/builtin functions 
# Example: len(), type(), range(), print()


# USER DEFINED FUNCTIONS:

# def Function_Name(argument):
    # body

def printName(fname, lname):    # Function definition
    print("Name:",fname, lname)

printName("Usman", "Khan")      # Function calling


a = 10
b = 8 

def isGreater(a,b):
    if (a>b):
        print("first number is greater")
    else:
        print("second number is greater or equals")

def isLesser(a,b):
    pass        # interpreter skips this functions until you complete it

isGreater(a,b)

# ARGUMENTS:

# Default Arguments:

# def sum(a=1, b=2):
#     print(a+b)
# sum() takes default arguments
# sum(4,10) skips the default argument and takes new one (4,10)
# sum(4) takes a as 4 and b remains default
# sum(b=9) takes b as 9 and a remains default

# Keyword Arguments:

# def sum(a,b):
#     print(a+b)
# sum(b=1, a=3) order of arguments does not matter


# Variable Length Arguments:

# def avg(*numbers):      # takes numbers as a tuple
#     sum = 0
#     for i in numbers:
#         sum = sum + i
#     print(sum/len(numbers))
# avg(5,6)
# avg(5,6,7,8)


# def printName(**name):      # takes name as dictionary
#     print("Hello,", name["fname"], name["mname"], name["lname"])
# printName(mname = "john", fname = "alex", lname = "Elia")


# RETURN:
def sum(a,b):
    return a+b      #returns the sum
c = sum(a,b)
print(c)