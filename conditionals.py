# MATHEMATICAL OPERATORS:
# +, -, *, /, %, //, **

# % -> modulo return the remainder of the division (4%2)
# // -> floor division, divides and round down the answer (5//2)
# ** -> power operator, base**power (2**2)  


# CONDITIONAL OPERATORS:
# >, <, >=, <=, ==, !=

# LOGICAL OPERATORS:
# and, or

# IF ELSE CONDITIONAL STATEMENTS:

num = int(input("enter a number: "))
# if (num > 0):
#     print("This is a positive number")
# elif (num == 0):
#     print("The number is zero")
# else:
#     print("This is a negative number")

if (num > 0):
    if (num >= 1 and num <= 10):            # NESTED IF
        print("the number is between 1 and 10")
    elif(num > 10 and num <= 20):
        print("the number is between 11 and 20")
    else:
        print("the number is greater than 20")
elif (num == 0):
    print("The number is zero")
else:
    print("This is a negative number")


# MATCH CASE STATEMENTS:

x = int(input("enter a number: "))
# match x:
#     case 0:
#         print("x is zero")
#     case 4:
#         print("case is 4")
#     case _:
#         print(x)

match x:
    case 0:
        print("x is zero")
    case 4:
        print("case is 4")
    case _ if x != 90:
        print(x, "is not 90")
    case _ if x != 80:
        print(x, "is not 80")
    case _:
        print(x)
    
