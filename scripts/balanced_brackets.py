"""a string of brackets passed in"""
bracket_string = input("Enter in a series of brackets")

# function balanced brackets takes one arg, a string of brackets


def check_balance(brackets):
    """Function determining balanced brackets"""
    # Add variable count, initiated to zero
    count = 0

    # Check to make sure if first character is opening, if so, return  false
    if brackets[0] == "]":
        return False

    # Iterate over the string
    for bracket in brackets:
        # If an open bracket, increment count
        if bracket == "[":
            count += 1
        # If a closing bracket, decrement count
        if bracket == "]":
            count -= 1
        # If count becomes negative, return False immediately
        if count < 0:
            return False

    # At the end, if count not equal to zero, return False, otherwise True
    return count == 0


print(check_balance(bracket_string))
