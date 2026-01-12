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
