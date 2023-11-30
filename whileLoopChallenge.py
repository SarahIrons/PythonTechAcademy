#WHILE LOOP CHALLENGE
#1. Execute a while loop.
i=0
while i <8:
    print(i)
    i+= 1
    
#2. Use the break statement within a while loop.
i=1
while i<5:
    print(i)
    if i==4:
        break
    i += 1
#3. Use the continue statement within a while loop.
i=0
while i<7:
    i +=1
    if i==4:
        continue
    print(i)
#4. Use the else statement within a while loop.
i=1
while i <8:
    print(i)
    i +=1
else:
        print("i is no longer less than 6")
