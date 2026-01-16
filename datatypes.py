# BOOLEAN:
# can only be True or False.
status = True
status = False
print(type(status))

# LIST:
# Multiple items stored under one single indentifier.
# data can be altered (lists are mutable).
# can store multiple data types.
# list = [a, b, c, d,...]
# Index   0, 1, 2, 3,...

list1 = [1, 2, "green", True, 0.3]
marks = [3, 5, 6]
# Index  0, 1, 2
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[-3])

if 7 in marks:
    print("7 is in the list")
else:
    print("7 is not in the list")

list2 = [i for i in range(10)]
print(list2)
list2 = [i for i in range(10) if i%2 == 0]
print(list2)

# LIST METHODS:
l = [1, 2, 3, 4]

print(len(l))  # returns the length of the list.
l.append(5)  # appends the argument in the list.
l.sort()  # sorts the list in ascending order.
l.sort(reverse=True)  # sorts the list in descending order.
l.reverse()  # reverses the order of the list.
print(l.index(3))  # l.index(value) returns the index of the first occurrence of the value in the list.
print(l.index(3, 0, 2)) # l.index(value, start, end) same as above but here it looks from start index to end index.
print(l.count(2))  # l.count(value) returns the number of time the value occurs in the list.
m = l.copy()  # l.copy() copies the list to another variable, the original list will remain unchanged.
l.insert(1, 9)  # l.insert(index, value) inserts the value at the index.
l.pop(0)  # l.pop(index) removes and return the value at the index.
n = [70, 80, 90]
l.extend(n)  # l.extend(n) extends the list by appending another given list.
k = l + n  # works same as above one but the l remains unchanged.   

# TUPLE:
# Multiple items stored under one single indentifier.
# data cannot be altered (tuples are immutable).
# can store multiple data types.
# tuple = (a, b, c, d,...)
# Index    0, 1, 2, 3,...

tup = (1, 2, "green", True, 0.3)
tup = (1, 2, 3)
print(tup)
print(type(tup)) 
print(tup[0])
print(tup[1])
print(tup[-3])
tup = (1,)  # for single data tuples comma should be added, else it will be considered as integer.

if 7 in tup:
    print("7 is in the tuple")
else:
    print("7 is not in the tuple")

# TUPLE METHODS:

# tuples are immutable so to alter its data first convert it into list then convert back to tuple.

countries = ("Spain", "England", "India", "Pakistan")
temp = list(countries)  # makes a list copy of countries
temp.append("Russia")
temp.pop(3)
temp[2] = "Finland"
countries = tuple(temp)
print(countries)

countries2 = ("China", "Egypt")
allCountries = countries + countries2   # concatenates 2 tuples
print(allCountries)

tup = (1,2,3,4,5)
print(tup.index(3))  # tup.index(value) returns the index of the first occurrence of the value in the tuple.
print(tup.index(3, 0, 2)) # tup.index(value, start, end) same as above but here it looks from start index to end index.
print(tup.count(2))  # tup.count(value) returns the number of time the value occurs in the tuple.
