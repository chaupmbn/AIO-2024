import math

# A function to check whether x is a number
def is_number(n):
    try:
        float(n)  # Type - casting the string to ‘float ‘.
                  # If string is not a valid ‘float ‘ ,
                  # it’ll raise ‘ValueError ‘ exception
    except ValueError:
        return False
    return True

# A function to calculate and print out value of activation function
def activation():
    print("---------------------------------------------------------")
    # Enter x
    x = input("Enter x: ")

    # Check whether x is a number; if not, exit the program
    if is_number(x) is False:
        print("x must be a number")
        return None

    # Enter activation function name
    func_name = input(
        "Enter name of the activation function (sigmoid, relu or elu): ")

    # Check whether the name of activation function is legitimate
    # if not, exit the program
    if func_name not in ["sigmoid", "relu", "elu"]:
        print(f"{func_name} is not supported")
        return None
    else:
        x = float(x)

    # Calculate and print out value of activation function
    if func_name == "sigmoid":
        sigmoid = 1 / (1 + math.e**(-x))
        print(f"Sigmoid: f({x}) = {sigmoid}")
    elif func_name == "relu":
        if x <= 0:
            relu = 0
        else:
            relu = x
        print(f"Relu: f({x}) = {relu}")
    else:
        if x <= 0:
            alpha = 0.01
            elu = alpha * (math.e**(x)-1)
        else:
            elu = x
        print(f"Elu: f({x}) = {elu}")


# Check test cases
activation()
activation()
activation()
activation()
activation()
