"""
Simple Fibonacci sequence recursive solution
Classic recursive fibonacci function has the time complexity 2^n and space complexity of n 
(which is the max callstack depth, ie. height of tree)
"""
from time import perf_counter

def fib(n):
    # base case (when n = 1 or 2):
    if n <= 2:
        return 1
       
    return fib(n-1) + fib(n-2)
    
# test cases
print(fib(6)) # should return 8
print(fib(7)) # should return 13
print(fib(8)) # should reutrn 21

# time test
startTime = perf_counter()
print(fib(35))
endTime = perf_counter()
print(f"Time test: {endTime - startTime:.5f} seconds")