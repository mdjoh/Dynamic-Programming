"""
canSum - see if you can make the given sum with elements from a list where elements can be used
more than once; return T or F

Memoized version
"""

def canSum(targetSum, numList, memo=None):
    # reset memo dictionary to empty
    if memo == None:
        memo = {}
        
    # base cases
    # check if in memo
    if targetSum in memo:
        return memo.get(targetSum)
    
    if targetSum == 0:
        return True
    elif targetSum < 0:
        return False
    
    for n in numList:
        remainder = targetSum - n
        if canSum(remainder, numList, memo):
            memo[targetSum] = True
            return True
            
    memo[targetSum] = False
    return False

    # store T/F as values in memo for caching but have return statements below to
    # have a return for top-level (ie. first) recursive function call

# test cases 
print(canSum(9, [2, 3])) # True
print(canSum(7, [2, 4])) # False
print(canSum(8, [5, 4, 3, 7])) # True
print(canSum(300, [7, 14])) # False

# =============================================================================
# Complexity of memoized method:
# let m be targetSum, n be list of numbers
# tree height = m thus, space complexity: O(m)
# time complexity: O(m * n)
# =============================================================================