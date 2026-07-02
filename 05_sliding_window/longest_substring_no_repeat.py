# What DS you use? 
# Loop over all the charecter O(n)
# Have a dictionary as seen = {} which holds the unique charecters
# Check if the char in seen
# If seen then 
# if not seen then
# Update the max_legth max(max_length, right-left+1) and return
# What is the time complexity? 
# O(n), O(k)
# What are the edge cases? 
# if empty then return 0. Fail fast. 
def longest_substring(string):
    seen = {}
    left = 0
    max_length = 0

    for right in range(len(string)):
        char = string[right]

        if char in seen and seen[char]>=left: 
            left = seen[char] + 1

        seen[char] = right
        max_length = max(max_length, right- left + 1)

    return max_length

print(longest_substring("abcabcbb"))
