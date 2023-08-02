#!/usr/bin/env python3
import logging

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

num1 = 10
num2 = 5

# Configure logging to show debug messages
logging.getLogger().setLevel(logging.DEBUG)

add_result = add(num1, num2)
logging.debug("Add: {} + {} = {}".format(num1, num2, add_result))

subtract_result = subtract(num1, num2)
print("Subtract: {} - {} = {}".format(num1, num2, subtract_result))

multiply_result = multiply(num1, num2)
print("Multiply: {} * {} = {}".format(num1, num2, multiply_result))

divide_result = divide(num1, num2)
print("Divide: {} / {} = {}".format(num1, num2, divide_result))
