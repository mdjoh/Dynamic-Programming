"""
canSum - see if you can make the given sum with elements from a list where elements can be used
more than once; return T or F

Brute force version
"""

from time import perf_counter

def canSum(targetSum, numList):
    # base cases
    if targetSum == 0:
        return True    
    elif targetSum < 0:
        return False

    # try out all numbers in numList
    for n in numList:
        remainder = targetSum - n
        if canSum(remainder, numList):
            return True
        
    return False

# test cases
print(canSum(7, [2, 3])) # True
print(canSum(7, [2, 4])) # False
print(canSum(8, [5, 4, 3, 7])) # True

# time test
startTime = perf_counter()
print(canSum(578, [15, 10, 7, 6, 5, 4, 2]))
endTime = perf_counter()
print(f"Time test: {endTime - startTime:.5f} seconds")

# =============================================================================
# Complexity of brute force method:
# let m be targetSum, n be list of numbers
# tree height = m thus, space complexity: O(m)
# time complexity: O(n^m)
# =============================================================================
