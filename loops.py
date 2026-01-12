# FOR LOOP:

name = "usman"
for i in name:
    print(i)

colors = ["red", "green", "yellow"]

for color in colors:
    print(color)
    for i in color:     # NESTED LOOP
        print(i)


# for i in range(stop)  iterates stop times from zero, does not include the stop.
for x in range(5):
    print(x)        # Prints 0 to 4, does not includes 5

# for i in range(start, stop)  iterates (stop-start) times from start, does not include stop.
for x in range(1, 5):
    print(x)        # Prints 1 to 4, does not include 5

# for i in range(start, stop, step)  iterates (stop-start) times from start, does not include stop and increments step, instead of 1, to i.
for x in range(0, 11, 2):
    print(x)        # Prints 1 to 10 and steps 2


# WHILE LOOP:

# while (condition) -> loops when the condition is true and stops when false.

i = 0
while (i < 5):
    print(i)    # loops 5 time 0 to 4
    i = i + 1

i = int(input("enter a number: "))
while (i >= 10):
    print(i)
    i = int(input("enter a number: "))

# while else
count = 5
while (count > 0):
    print(count)    # loops 5 time from 5 to 1
    count = count - 1
else:
    print("i am inside else section, outside the loop")


# DO WHILE LOOP:
# there is no do while loop in python but we can emulate it, here's how

i = 0
while (True):
    print(i)
    i = i+1
    if i >= 5:    # a do while loop which loops 5 times
        break

