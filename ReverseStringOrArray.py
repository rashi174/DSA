'''
Given a string S as input. You have to reverse the given string.

Input: First line of input contains a single integer T which denotes the number of test cases. T test cases follows, first line of each test case contains a string S.

Output: Corresponding to each test case, print the string S in reverse order.

Constraints:
1 <= T <= 100
3 <= length(S) <= 1000

Example:
Input:
3
Geeks
GeeksforGeeks
GeeksQuiz

Output:
skeeG
skeeGrofskeeG
ziuQskeeG

'''

# o(n)- Time & O(1)- Space


testcase=int(input())
for _ in range(testcase):
    s=input()
    s=list(s)
    st=0
    end=len(s)-1
    while(st<end):
        s[st],s[end]=s[end],s[st]
        st+=1
        end-=1
    print(''.join(s))
    


#Recursive solution


def reverseList(A, start, end):
	if start >= end:
		return
	A[start], A[end] = A[end], A[start]
	reverseList(A, start+1, end-1)


    


#using Slicing
 
 print(s[::-1])
 
