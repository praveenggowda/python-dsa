def most_water_container(heights):
    right = len(heights) - 1
    left = 0
    height = 0
    distance = 0
    max_area = 0

    while left < right:
        height = min(heights[left], heights[right])
        distance = right - left 
        area = height * distance

        if area > max_area:
            max_area = area

        if(heights[left] < heights[right]):
            left += 1
        else: 
            right -= 1
        

    return max_area

print(most_water_container([]))
print(most_water_container([1, 8, 6, 2, 5, 4, 8, 3, 7]))
