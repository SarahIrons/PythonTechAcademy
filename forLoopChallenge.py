#FOR LOOP CHALLENGE

#1.Execute a for loop.
colors=["blue", "red", "yellow"]
for x in colors:
    print(x)
#2.Use the break statement within a for loop.
nouns=["person", "place", "thing", "idea"]
for x in nouns:
    print(x)
    if x=="thing":
        break
#3. Use the continue statement within a for loop.
names=["Arthur","Chet","Simon","Buster"]
for x in names:
    if x =="Simon":
        continue
    print(x)
#4. Use the range() function within a for loop.        
for (i) in range(4):
    print(i)
#5. Use the else keyword within a for loop.
for (i) in range (5):
    print(i)
else:
    print("All numbers printed in range!")
    
