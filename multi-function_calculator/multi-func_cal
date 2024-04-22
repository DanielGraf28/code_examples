import math
import sympy
from sympy import symbols
from sympy.solvers import solve


def addition():
    a = float.input("Enter first number: ")
    b = float.input("Enter second number: ")
    answer = a+b
    return answer
def subtraction():
    a = float.input("Enter first number: ")
    b = float.input("Enter second number: ")
    answer = a-b
    return answer
def multiply():
    a = float.input("Enter first number: ")
    b = float.input("Enter second number: ")
    answer = a*b
    return answer
def division():
    a = float.input("Enter first number: ")
    b = float.input("Enter second number: ")
    answer = a/b
    return answer
def prime_detector():
    number = int(input("Enter a positive integer: "))
    prime_or_comp = "prime"

    for test_number in range(2,number):
        if number%test_number==0:
            prime_or_comp = "composite"
    return prime_or_comp
def prime_factors():
    number = int(input("Enter a positive integer: "))
    factors = []
    divisor = 2
    while divisor <= number:
        if number % divisor == 0:
            factors.append(divisor)
            number = number // divisor
        else:
            divisor += 1
    return factors
def sqrt_funtion():
    n = int(input('Without the radical, enter a square root to factor: '))

# Use these variables
    upper_limit = math.floor(math.sqrt(n)) + 1
    max_factor = 1
    other_factor = 1
    square_root = 1

# Notice what the loop is doing here
    for maybe_factor in range(1, upper_limit):
        if n % (maybe_factor**2) == 0:
            max_factor = maybe_factor**2

# Divide out the greatest square factor
    other_factor = n/max_factor

    square_root = int(math.sqrt(max_factor))
    other_factor = int(other_factor)
    output = square_root*sympy.sqrt(other_factor)
    return output
def find_var():

    x = symbols('x')

    eq = input('Enter an equation to solve for x: 0 = ')
    print(len(solve(eq,x)))
    print("x = ", solve(eq,x)[0])

print(" 1 for addition\n 2 for subtration\n 3 for multipcation\n 4 for division\n 5 for to check if prime number\n 6 for list of prime factors\n 7 for square root\n 8 to find a variable")
choice = int(input("Please select a interger between 1 and 8: "))
if choice == 1:
    addition()
elif choice == 2:
    subtraction()
elif choice == 3:
    mutiply()
elif choice == 4:
    division()
elif choice == 5:
    prime_detector()
elif chocie == 6:
    prime_factors()
elif choice == 7:
    sqrt_funtion()
elif choice == 8:
    find_var()
