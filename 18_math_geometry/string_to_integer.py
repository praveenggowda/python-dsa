def my_atoi(string_number):
    result = 0
    sign = 1
    
    if not string_number:
        return 0
    
    s = string_number.lstrip()

    for num in s:   
        if num.isdigit():
            result = result * 10 + int(num)
        elif num =='-':
            sign = -1
        elif num =='+':
            sign = 1
        else:
            break

    result = result * sign

    if result > (2**31 - 1) or result < -(2**31):
        return 0;

    return result

print(my_atoi("123"))     # 123
print(my_atoi("-123"))    # -123
print(my_atoi("  42"))    # 42
print(my_atoi("42abc"))   # 42
print(my_atoi(""))        # 0


        
        
    


