"""Group 1"""
#function to print greater value
def greater(a,b):
    if a>b:
        print("{} is greater.".format(a))
    elif b>a:
        print("{} is greater.".format(b))
    else:
        print("{o} = {t}".format(o = a, t = b))

#the input variables
first  = float(input("Input the first digit: "))
second = float(input("Input the second digit: "))

#calling the function giving the above variables as arguments
greater(first,second)