#https://www.interviewbit.com/problems/trailing-zeros-in-factorial/
'''
____Trailing Zeroes in factorial_____

Given an integer n, return the number of trailing zeroes in n!.
Note: Your solution should be in logarithmic time complexity.

Example :

n = 5
n! = 120 
Number of trailing zeros = 1
So, return 1

'''

class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, n):
        c=0
        while n>=5:
            n=n//5
            c=n+c
        return (c)   
    
    
        
