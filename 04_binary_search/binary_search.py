def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1
    index = -1 
    
    while (left <= right):
        mid = (left + right) // 2

        if numbers[mid] == target:
            return mid
       
        if numbers[mid] > target:
            right = mid - 1
        else:   
            left = mid + 1 

    return index

print(binary_search([], 0))
print(binary_search([1, 2, 3, 4], 5))
print(binary_search([1, 3, 5, 7, 9], 3))
print(binary_search([1, 3, 5, 7, 9], 3))
print(binary_search([1, 3, 5, 7, 9, 11, 13], 9))


