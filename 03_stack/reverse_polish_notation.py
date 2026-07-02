def eval_rpn(tokens):
    stack = []
    result = 0

    for item in tokens:
        if item in {'+', '-', '*', '/'}:
            b = stack.pop()
            a = stack.pop()

            if item == '+':
                result = a + b
            elif item == '-':
                result = a - b
            elif item == '*':
                result = a * b
            elif item == '/':
                result = int(a / b)
            
            if result > (2**31-1) or result < -(2**31):
                return 0
            else:
                stack.append(result)
        else:   
            stack.append(int(item))
    
    return stack[0]

print(eval_rpn(["2", "1", "+", "3", "*"]))
print(eval_rpn(["4", "13", "5", "/", "+"]))
print(eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
