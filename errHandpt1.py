
def getInfo():
    var1 = input("\nPlease provide the first numeric value: ")
    var2 = input("\nPlease provide the second numeric value: ")
    return var1,var2

def compute():
    go=True
    while go:
        var1,var2=getInfo()
        try:
            var3 = int(var1) + int(var2)
            go=False
        except ValueError as e:
            print("It appears you did not enter a numeric value; please try again.".format(e))
    print("{} + {} = {}".format(var1, var2, var3))

if __name__ == "__main__" :
    compute()




