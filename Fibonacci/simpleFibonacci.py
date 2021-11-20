# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 16:28:34 2021

@author: Marchiano
Simple Fibonacci sequence recursive solution
Classic recursive fibonacci function has the time complexity 2^n and space complexity of n 
(which is the max callstack depth, ie. height of tree)
"""
import time

def fib(n):
    # base case (when n = 1 or 2):
    if n <= 2:
        return 1
       
    return fib(n-1) + fib(n-2)
    
# test cases
print(fib(6)) # should return 8
print(fib(7)) # should return 13
print(fib(8)) # should reutrn 21

# time code
startTime = time.process_time()
print(fib(35))
print("%.5f seconds" % (time.process_time() - startTime))
