"""
shortestSum - return an array that represents the shortest combination to make up 
a target sum from an array of positive integers. The same integer from the 
number array can be used multiple times.
In the event of multiple arrays with the shortest length, return any one of those arrays.
If there is no way to make the target sum from given number array, return None.

Example: target sum = 5, number array = [1, 2, 3]
While [1, 2, 2], [1, 1, 1, 2], [1, 1, 3], [2, 3] all sum to 5, the function 
returns the array [2, 3] because it is the shortest in length

Memoized method
"""

def shortestSum(targetSum, numList, memo=None):
    
    # reset memo dictionary to empty if None is passed
    if memo is None:
        memo = {}
        
    # Base Cases
    # check if targetSum is in memo
    if targetSum in memo:
        return memo.get(targetSum)
    
    # check if targetSum is already in numList and if True, 
    # return array of length of 1 with targetSum as the only element
    if targetSum in numList:
        return [targetSum]
    elif targetSum == 0:
        return []
    elif targetSum < 0:
        return None
    
    optimalSolution = None # initialize optimalSolution to None and return None 
                           # if no possible combinations are found
    
    for n in numList:
        remainder = targetSum - n       
        combination = shortestSum(remainder, numList, memo)

        if combination is not None:
            possibleSolution = combination.copy()
            possibleSolution.append(n)
            
            # check if the current possible solution is the shorter than the current optimal solution
            if (optimalSolution is None) or (len(possibleSolution) < len(optimalSolution)):
                optimalSolution = possibleSolution
    
    memo[targetSum] = optimalSolution
    return optimalSolution

# Test Cases
print(shortestSum(8, [5, 3, 2])) # [5,3]
print(shortestSum(8, [5, 1, 4])) # [4,4]
print(shortestSum(4, [2, 4])) # [4]
print(shortestSum(0, [1, 2, 7])) # []
print(shortestSum(7, [2, 4, 6])) # None
print(shortestSum(100, [2, 5, 25])) # [25, 25, 25, 25]

# =============================================================================
# Complexity of memoized method:
# let m be targetSum, n be length of array of numbers
# max possible number of memo keys = m; max possible value storage size in memo = m
# Thus, space complexity: O(m * m)
# time complexity: O(m * n * m) -> m*n because checking for every element in 
# numList for m possible keys in memo then * m because copying each element in the list
# every time append is called
# =============================================================================