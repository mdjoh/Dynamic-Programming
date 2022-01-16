"""
howSum - return in an array one way the target sum can be made with a given list of positive integers
Numbers in the list can be used more than once

If the targetSum cannot be made using numbers from the list, then return None

Brute force method
"""

from time import perf_counter

def howSum(targetSum, numList, memo=None):
    
    # reset memo to empty if None is passed
    if memo is None:
        memo = {}
        
    # Base Cases
    # check if targetSum is in memo
    if targetSum in memo:
        return memo.get(targetSum)
    
    if targetSum < 0:
        return None
    elif targetSum == 0:
        return [] # return empty array because no elements in numList sum to 0
    
    
    for n in numList:
        remainder = targetSum - n
        combo = howSum(remainder, numList, memo)
        if combo is not None:
            combo.append(n) # copies combo list each time when append is called
            memo[targetSum] = combo
            return combo
    
    # return None if a valid combo of addends is not found after for loop
    memo[targetSum] = None
    return None 

# Test Cases
print(howSum(-1, [7, 2, 5]))
print(howSum(0, [7, 2, 5]))
print(howSum(7, [3, 2]))
print(howSum(10, [2, 3, 5]))

# Time Test
startTime = perf_counter()
print(howSum(300, [7, 14]))
endTime = perf_counter()
print(f"Time test: {endTime - startTime:.5f} seconds")

# =============================================================================
# Complexity of memoized method:
# let m be targetSum, n be length of list of numbers
# tree height = m thus, space complexity: O(m * m) -> memo is the main space user
# memo would have at most m number of keys with a value of array of length m
# time complexity: O(n*m* m) -> * m because copying of each element in the list 
# each time append is called
# memoized solution is faster but uses more space than the brute force solution
# =============================================================================