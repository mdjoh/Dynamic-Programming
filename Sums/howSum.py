"""
howSum - return in an array one way how the target sum can be made with a given list of positive integers
Numbers in the list can be used more than once

If the targetSum cannot be made using numbers from the list, then return None

Brute force method
"""

def howSum(targetSum, numList):
        
    # Base Cases
    if targetSum < 0:
        return None
    elif targetSum == 0:
        return [] # return empty array because no elements in numList sum to 0
    
    
    for n in numList:
        remainder = targetSum - n
        combo = howSum(remainder, numList)
        if combo is not None:
            combo.append(n) # copies combo list each time when append is called
            return combo
    
    return None # return None if a valid combo of addends is not found after for loop

# Test Cases
print(howSum(-1, [7, 2, 5]))
print(howSum(0, [7, 2, 5]))
print(howSum(7, [3, 2]))
print(howSum(10, [2, 3, 5]))

# =============================================================================
# Complexity of brute force method:
# let m be targetSum, n be length of list of numbers
# tree height = m thus, space complexity: O(m)
# time complexity: O(n^m * m) -> * m because copying of list each time append 
# is called
# =============================================================================