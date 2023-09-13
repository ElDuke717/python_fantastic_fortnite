
def balanced_brackets(brackets):
    if len(brackets) == 0 or brackets == " ":
        return False
    stack = []
    for bracket in brackets:
        if bracket == "[":
            stack.append(bracket)
        elif bracket == "]":
            if not stack:  # Stack is empty, can't pop, thus not balanced
                return False
            stack.pop()

    # At this point, stack should be empty for brackets to be balanced
    return len(stack) == 0


# Test the function
bracket_string = input("Enter in a series of brackets: ")
print(balanced_brackets(bracket_string))
