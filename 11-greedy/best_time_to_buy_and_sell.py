"""
Problem: Best Time to Buy and Sell Stock
LeetCode: 121
Category: Greedy
Difficulty: Easy

Problem Statement:
You are given an array prices where prices[i] is the price of a stock on day i.
You want to maximise your profit by choosing a single day to buy and a different
later day to sell. Return the maximum profit. If no profit is possible, return 0.

Examples:
Input: prices = [7,1,5,3,6,4]  ->  Output: 5
Input: prices = [7,6,4,3,1]    ->  Output: 0

Clarifications:
- Must buy before you sell
- Cannot buy and sell on the same day
- If no profit possible, return 0

Brute Force:
Two nested loops, check every buy/sell pair
Time: O(n²)  Space: O(1)

Optimized Approach:
Track minimum price seen so far
At each step calculate profit = price - min_price
Track maximum profit seen

Complexity:
Time Complexity: O(n)
Space Complexity: O(1)

Pattern: Greedy
"""

def max_profit(prices: list[int]) -> int:

    if not prices:
        return 0
    
    min_price = prices[0]
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)       
    
    return max_profit

print(max_profit([7, 1, 5, 3, 6, 4]))  # 5
print(max_profit([7, 6, 4, 3, 1]))     # 0
print(max_profit([1]))                 # 0
print(max_profit([]))                  # 0
