def add(x, y):      # method of addition, which takes two parameters x and y and returns the addition of them
    return x + y

def subtract(x, y):     # method of subtraction of two numbers
    return x - y

def multiply(x, y):     # method of multiplication of two numbers
    return x * y

def divide(x, y):       # method of division of two numbers
    if y == 0:
        return "Can not divide by zero!"
    return x/y

def main():
    while True:
        print("Operations:")
        print("Enter 'add' to add two numbers")
        