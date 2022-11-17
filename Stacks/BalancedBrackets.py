def is_balanced(string):
    brackets = {")": "(", "]": "[", "}": "{"}
    stack = []

    for bracket in string:
        if bracket in brackets.values():
            stack.append(bracket)
        else:
            if not stack or brackets[bracket] != stack.pop():
                return False

    return not stack
