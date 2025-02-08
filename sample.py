import random 

def get_random_number():
    return random.randint(1, 100)

def print_message():
    number = get_random_number()
    if number % 2 == 0:  # Syntax Error (= should be ==)
        print("Even number:", number)
    else:
        print("Odd number:", number)  # Syntax Error (missing colon)

print_message()
