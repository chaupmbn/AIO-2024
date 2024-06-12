# Import needed library
import math
import random

# Define support functions


def mae(target, pred):
    return abs(target - pred)


def mse(target, pred):
    return (target - pred)**2


def rmse(target, pred):
    return mse(target, pred)**0.5


def generate():
    target = random.uniform(0, 10)
    pred = random.uniform(0, 10)
    return target, pred

# Define main function


def loss_function():
    print("---------------------------------------------------------")
    num_samples = input("Enter number of samples:")
    # Check whether input is a number
    if num_samples.isnumeric() is False:
        print("Number of samples must be an integer number")
        return None
    num_samples = int(num_samples)  # convert to integer number
    loss_name = input("Enter name of loss function (mae, mse or rmse):")
    result = 0
    if loss_name == "mae":
        for i in range(num_samples):
            target, pred = generate()  # genrate randomly target and predict numbers
            loss = mae(target, pred)
            result += loss
            print(
                f"Loss name: {loss_name}, sample : {i}, pred: {pred}, target: {target}, loss: {loss}")
        print(f"Final MAE: {result/ num_samples}")
    elif loss_name == "mse":
        for i in range(num_samples):
            target, pred = generate()  # genrate randomly target and predict numbers
            loss = mse(target, pred)
            result += loss
            print(
                f"Loss name: {loss_name}, sample : {i}, pred: {pred}, target: {target}, loss: {loss}")
        print(f"Final MSE: {result/ num_samples}")
    elif loss_name == "rmse":
        for i in range(num_samples):
            target, pred = generate()  # genrate randomly target and predict numbers
            loss = rmse(target, pred)
            result += loss
            print(
                f"Loss name: {loss_name}, sample : {i}, pred: {pred}, target: {target}, loss: {loss}")
        print(f"Final RMSE: {result/ (num_samples)**0.5}")
    else:
        print(f"{loss_name} is not supported")
        return None


# Check test cases
loss_function()
loss_function()
loss_function()
