def check_braces(input_str):
    stack = []
    matching_braces = {')': '(', ']': '[', '}': '{'}
    
    for char in input_str:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != matching_braces[char]:
                return "Error: Mismatched or unclosed braces"
            stack.pop() 
    
    if stack:
        return "Error: Unmatched opening brace"
    else:
        return "Braces are properly closed!"

input_str = "set={ (9[23),4"
print(check_braces(input_str))
