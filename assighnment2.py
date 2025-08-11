import math

try:

    number= float(input("Enter a number: "))
    square_root = math.sqrt(number)



    natural_logarithm = math.log(number)


    sine_value = math.sin(number)


    print(f"The square root of {number} is: {square_root}")
    print(f"The natural logarithm (log base e) of {number} is: {natural_logarithm}")
    print(f"The sine of {number} (in radians) is: {sine_value}")

except ValueError:
    print("Invalid input. Please enter a valid numerical value.")
input("Press ENTER to exit")#just for saving purposes