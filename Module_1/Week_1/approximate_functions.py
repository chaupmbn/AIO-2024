# Define a function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        result = 1
    else:
        result = n * factorial(n-1)
    return result

def sin(x, n):
    result = 0
    for i in range(n):
        result += ((-1)**i) * (x**(2*i+1)) / factorial(2*i+1)
    print(f"Approximate of sin({x}) with n = {n}:")
    print(result)

def cos(x, n):
    result = 0
    for i in range(n):
        result += ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i)
    print(f"Approximate of cos({x}) with n = {n}:")
    print(result)

def sinh(x, n):
    result = 0
    for i in range(n):
        result += (x ** (2 * i + 1)) / factorial(2 * i + 1)
    print(f"Approximate of sinh({x}) with n = {n}:")
    print(result)

def cosh(x, n):
    result = 0
    for i in range(n):
        result += (x ** (2 * i)) / factorial(2 * i)
    print(f"Approximate of cosh({x}) with n = {n}:")
    print(result)

# Check test cases
sin(x=3.14, n=10)
cos(x=3.14, n=10)
sinh(x=3.14, n=10)
cosh(x=3.14, n=10)
