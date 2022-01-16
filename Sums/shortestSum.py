"""
shortestSum - return an array that represents the shortest combination to make up 
a target sum from an array of positive integers. The same integer from the 
number array can be used multiple times.
In the event of multiple arrays with the shortest length, return any one of those arrays.
If there is no way to make the target sum from given number array, return None.

Example: target sum = 5, number array = [1, 2, 3]
While [1, 2, 2], [1, 1, 1, 2], [1, 1, 3], [2, 3] all sum to 5, the function 
returns the array [2, 3] because it is the shortest in length

Brute force method taking into account Python memory allocation intricacy
Array memory allocation in Python can cause unexpected outputs
"""

def shortestSum(targetSum, numList):
        
    # Base Cases
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
        combination = shortestSum(remainder, numList)

        if combination is not None:
            # need to create a copy of combination and append to the copy
            possibleSolution = combination.copy() 
            possibleSolution.append(n)
            
            # check if the current possible solution copy is the shorter than the current optimal solution
            if (optimalSolution is None) or (len(possibleSolution) < len(optimalSolution)):
                optimalSolution = possibleSolution
            
            # if combination was appended to, optimalSolution and combination will point to the same
            # array in memory giving unexpected outputs
            
    return optimalSolution

# Test Cases
print(shortestSum(8, [5, 3, 2])) # [5,3]
print(shortestSum(8, [5, 1, 4])) # [4,4]
print(shortestSum(4, [2, 4])) # [4]
print(shortestSum(0, [1, 2, 7])) # []
print(shortestSum(7, [2, 4, 6])) # None
print(shortestSum(25, [2, 5])) # [5, 5, 5, 5, 5]

# =============================================================================
# Complexity of brute force method:
# let m be targetSum, n be length of array of numbers
# stack depth = m
# max possible optimalSolution storage size for every recursion call (ie stack frame) = m
# Thus, space complexity: O(m * m)
# time complexity: O(n^m * m) -> * m because copying each element in the list
# every time append is called
# =============================================================================