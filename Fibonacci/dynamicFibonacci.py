# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 18:24:52 2021

@author: Marchiano

Fibonacci function solved with dynamic programming (instances of same subproblems that make up a larger problems
and use solution from first subproblem to solve identical future subproblems - technique is called
memoization)

"""
import time

# best way to implement memoization: use fast-access data structure such as a HashMap equivalent
# which is a dictionary in Python

# keys: function argument  values: return value

def fib(n, memo = {}): # memo is an optional argument with an empty dictionary as its default value
# default value will be used if memo isn't passed in in a fib call
    
    # base case 1:
    # check if current argument is inside memo and if so, return value for current argument key
    if n in memo:
        return memo.get(n)
    
    # base case 2:
    if n <= 2:
        return 1
    
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo.get(n)

# test cases
print(fib(6)) # should return 8
print(fib(7)) # should return 13
print(fib(8)) # should reutrn 21

# time code
startTime = time.process_time()
print(fib(300))
print("%.5f seconds" % (time.process_time() - startTime))

# memoizing makes the time complexity a linear one (O(n) time complexity) from an exponential one 
# -> RUNS A LOT FASTER
# space complexity is still O(n)
