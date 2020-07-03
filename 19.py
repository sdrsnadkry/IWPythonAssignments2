def is_valid(strings):
    stack = []
    dictonary = {"(": ")", "{": "}", "[": "]"}

    for item in strings:
        if item in dictonary:
            stack.append(item)

        elif dictonary[stack.pop()] != item:
            return False

    return len(stack) == 0  #return False if any one paranthesis remains un popped


print(is_valid("(){[]}"))
print(is_valid("({)}"))
