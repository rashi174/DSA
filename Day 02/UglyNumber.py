'''
Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers. By convention, 1 is included.

Given a number n, the task is to find n’th Ugly number.

Examples:

Input  : n = 7
Output : 8

Input  : n = 10
Output : 12

Input  : n = 15
Output : 24

Input  : n = 150
Output : 5832

'''
class Solution:
    def isUgly(n):
        while n%2==0 or n%5==0 or n%3==0:
            if n%2==0:
                n=n//2
            elif n%3==0:
                n=n//3
            else:
                n=n//5
        return True if n==1 else False

    def getNthUglyNo(self,nth):
        i=1
        c=1
        while nth>c:
            i+=1
            if Solution.isUgly(i)==True:
                c+=1
        return i
ob=Solution()
result=ob.getNthUglyNo(150)
print(result)
