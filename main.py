#WRITE YOUR CODE IN THIS FILE
def factorial(x):
    # define the function with 1 parameter
    y=1
    #create variable to represnt the number that will
    for i in range(1,x):
        y= y * i
    return y
print(factorial())
        