import math

def calculate_area(radius):
    pi = 3.14159
    area = pi * radius * radius  # Correct calculation, but forgot to check for negative radius
    return area

def print_area(radius):
    area = calculate_area(radius)
    print("Area of the circle: " + area)  # TypeError: 'area' is a float, can't concatenate with a string

def unused_function(x):
    unused_variable = 10  # Unused variable
    return x * 2

def long_function():
    # This function is too long and does too many things
    x = 10
    y = 20
    z = 30
    a = x + y + z
    b = a * 2
    c = b - 5
    d = c * 3
    e = d / 4
    f = e + 1
    g = f * 2
    h = g - 7
    return h

def main():
    print_area(-5)  # Logic error: radius cannot be negative for calculating area
    unused_function(5)
    long_function()

main()
