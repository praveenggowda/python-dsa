def reverse_string(digits):
    result = 0
    
    while digits != 0:
        lastDigit = digits % 10
        result = result * 10 + lastDigit
        digits = digits // 10

    if result > 2**31 - 1 or result < -(2**31):
        return 0
    
    return result
        
print(reverse_string(345))