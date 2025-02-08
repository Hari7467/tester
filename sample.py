def calculate_area(radius):
    pi = 3.14159
    area = pi * radius * radius  # Correct calculation, but we forgot to check for negative radius
    
    return area

def print_area(radius):
    area = calculate_area(radius)
    print("Area of the circle: " + area)  # Type Error: 'area' is a float, can't concatenate with a string

def main():
    print_area(-5)  # Logic error: radius cannot be negative for calculating area

main()
