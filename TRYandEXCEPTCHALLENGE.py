#TRY EXCEPT & FINALLY CHALLENGE
#Execute a try block, except block and finally block.

a=10
b=0
try:
    c = a / b
    print(c)
except ZeroDivisionError as error:
        print(error)
finally:
            print('The statements have been executed and we are finishing up.')
            
