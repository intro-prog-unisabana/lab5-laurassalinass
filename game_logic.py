from secret_number import seed_secret_numbers, generate_secret_number
from response import input_response

print("Enter a seed number:")
seed = int(input(""))

value = False

seed_secret_numbers(seed)
generate_value = generate_secret_number(1, 100)

while value == False:
    print("What is your guess:")
    user_input = int(input(""))
    value = input_response(generate_value, user_input)