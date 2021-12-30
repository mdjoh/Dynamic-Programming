"""
Find the number of ways you can move through a m-by-n 
grid only by going down or right

Solved with memoization
"""

def grid_traveler(m, n, memo={}):
    # base cases
    # check if m,n combo (of tuple type) is in memo; use tuple since it's immutable
    if (m, n) in memo:
        return memo.get((m, n))
    
    if m == 1 and n == 1:
        return 1
    
    elif m == 0 or n == 0:
        return 0
    
    memo[(m, n)] = grid_traveler(m-1, n, memo) + grid_traveler(m, n-1, memo)
    return memo.get((m, n))

# test cases
print(grid_traveler(1,1)) # should be 1
print(grid_traveler(2,3)) # should be 3
print(grid_traveler(18,18)) # should be 2333606220

# time complexity is O(m*n); m*n gives the number of distinct nodes possible 
# which is also the number of times grid_traveler function is called

# space complexity is the same as brute force example O(m+n)