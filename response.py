def input_response(generate_value, user_input):
    if generate_value > user_input:
        print("Too low! Try a higher number.\n")
        value = False
    elif generate_value < user_input:
        print("Too high! Try a lower number.\n")
        value = False
    elif generate_value == user_input:
        print("Correct! You guessed the number!\n")
        value = True

    return value
    