# --STRING BUILT-IN FUNCTIONS--
name = "usman"
string = "Hello Hello!!!"

print(len(name))  # len(string) returns the length of the string.

print("my age is", 19)

print(name + " " + string)  # Concatenation

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

# string.center() --> centers the string by adding padding on both sides
print(name.center(50))  # string.center(width) changes the width/length to width (i.e 50) and centers the string.
print(name.center(50, "."))  # string.center(width, fillchar) it also works the same as above but it adds the fillchar on both sides.

print(string.count("hell"))  # string.count(value) returns the number of time the value has occured in the string.

print(name.endswith("an"))  # string.endswith(value) return true if the string ends with the value otherwise false.
print(name.endswith("ma", 1, 3))  # string.endswith(value, startindex, endindex) works the same as above but it checks within the startindex to endindex.
print(name.startswith("us"))  # string.startswith(value) return true if the string starts with the value otherwise false.
print(name.startswith("sm", 1, 3))  # string.startswith(value, startindex, endindex) works the same as above but it checks within the startindex to endindex.


print(string.find("lo"))  # string.find(value) returns the index of the first occurrence of the value in the string if it exists, -1 otherwise.

print(name.isalnum())  # string.isalnum() returns true if the string is alphanumeric (A-Z,a-z,0-9), false otherwise.
print(name.isalpha())  # string.isalpha() returns true if the string is alpha (A-Z,a-z), false otherwise.
print(name.isdigit())  # string.isdigit() returns true if the string is a number (0-9), false otherwise.
print(name.islower())  # string.islower() returns true if the string is lower case, false otherwise.
print(name.isupper())  # string.isupper() returns true if the string is upper case, false otherwise.
print(name.isprintable())  # string.isprintable() returns true if the string is printable (not having characters like \n etc.), false otherwise.
print(name.isspace())  # string.isspace() returns true if the string contains only whitespaces, false otherwise.
print(string.istitle()) # string.istitle() return true only if the first letter of each word is capital in the string, false otherwise.

print(string.swapcase())  # string.swapcase() converts the upper case characters to lower case and lower to upper.

print(string.title())  # string.title() capitalizes the first character of each word.