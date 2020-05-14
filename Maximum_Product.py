#https://www.interviewbit.com/problems/highest-product/
'''

Given an array A, of N integers A.

Return the highest product possible by multiplying 3 numbers from the array.

NOTE: Solution will fit in a 32-bit signed integer.



Input Format:

The first and the only argument is an integer array A.

Output Format:

Return the highest possible product.

Constraints:

1 <= N <= 5e5

Example:

Input 1:
A = [1, 2, 3, 4]

Output 1:
24

Explanation 1:
2 * 3 * 4 = 24

Input 2:
A = [0, -1, 3, 100, 70, 50]

Output 2:
350000

Explanation 2:
70 * 50 * 100 = 350000

'''

class Solution:
	# @param A : list of integers
	# @return an integer
	def maxp3(self, nums):
	    asc=sorted(nums)
	    dsc=asc[::-1]
        p=asc[0]*asc[1]
        return max(p*dsc[0],dsc[0]*dsc[1]*dsc[2])

