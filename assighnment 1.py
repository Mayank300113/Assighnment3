
def factorial(n):

    if n<2:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("Enter a number:"))
result=factorial(n)
print("The factorial of this number is",result)
input("Press ENTER to exit")#just for saving purposes