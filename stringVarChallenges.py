##STRING VARIABLE CHALLENGES

##Assign a string to a variable.
varA = "Carlo is a cat."
print (varA)
##Assign a multiline string to a variable.
varB = """so much depends\n
upon\n
\n
a red wheel\r
barrow\r
\r
glazed with rain\r
water\r
\r
beside the white\r
chickens"""

print("/r")

print(varB)
##Return a range of characters by using the slice syntax.
a = ("apple","pizza","pie")
b = slice(1)
print(a[b])

##Use the len() function.
pyList = ["apple","pizza","pie"]
a=len(pyList)
print(a)
##Use the strip() method.
messageDisplay = "    Here is the message  "
print("Update:", messageDisplay.strip())
##Use the upper() method.
messageDisplay = "no need to shout"
print(messageDisplay.upper())

##Use the in or not in keyword to check whether or not a particular phrase or character is present in a string.
Nephews = ["Bob", "Casey","Frank", "Pete"]
print("Bob" not in Nephews)
print("Joe" not in Nephews)

##Concatenate a string.
part1 = "The cats "
part2 = "ate breakfast already."
part3 = part1 + part2
print(part3)
##Use an escape character.
txt="this is a line\nand this is a new line!"
print(txt)
