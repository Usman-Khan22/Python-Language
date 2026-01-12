# --STRING BUILT-IN FUNCTIONS--
name = "usman"
string = "hello!!"

print(len(name))  # len(string) returns the length of the string.

# PRINTING/ACCESSING EACH CHARACTER OF A STRING:
for character in name:
    print(character)

# name[a:b] --> including a but not b
print(name[0:3])  # returns the string from 0th index to 2nd index. 
print(name[:3])   # works same as above -> (name[0:3]).
print(name[2:4])  # returns the string from 2nd index to 3rd index.
print(name[-4:-2])  # works like this -> name[len(name)-4:len(name)-2] -> name[1:3].

print(name.upper())  # string.upper() converts the string to upper case.
print(name.lower())  # string.lower() converts the string to lower case.

print(string.rstrip("!"))  # string.rstrip(character) removes the trailing characters from the string.
print(string.split(" "))  # string.split(delim) seperates and stores the string, in a list, on the basis of the delim e.g (" ").
print(name.replace("usman", "john"))  # string.replace(string1, string2) replaces all the occurrences of string1 to string2.
print(name.capitalize())  # string.capitalize() capatilizes the first character of the string.