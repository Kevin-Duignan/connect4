# Oliver
def validate_input(prompt, valid_inputs):
    """
    Repeatedly ask user for input until they enter an input
    within a set valid of options.

    :param prompt: The prompt to display to the user, string.
    :param valid_inputs: The range of values to accept, list
    :return: The user's input, string.
    """
    # Implement your solution below
    print(prompt, end="")
    enter = input()
    if enter in valid_inputs:
        return enter
    else:
        print("Invalid input, please try again.")
        return validate_input(prompt, valid_inputs)


if __name__ == "__main__":
    # Enter test code below
    user_input = validate_input(
        "Please select an option (a, b, c): ", ["a", "b", "c"])
