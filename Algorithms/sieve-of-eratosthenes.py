'''
Sieve of Eratosthenes 

Given a number N, calculate the prime numbers up to N using Sieve of Eratosthenes.  

Example 1:

Input:
N = 10

Output:
2 3 5 7

Explanation:
Prime numbers less than equal to N 
are 2 3 5 and 7.
Example 2:

Input:
N = 35

Output:
2 3 5 7 11 13 17 19 23 29 31

Explanation:
Prime numbers less than equal to 35 are
2 3 5 7 11 13 17 19 23 29 and 31.

Your Task:  
You don't need to read input or print anything. Your task is to complete the function sieveOfEratosthenes() which takes an integer N as an input parameter and return the list of prime numbers less than equal to N.

Expected Time Complexity: O(NloglogN)
Expected Auxiliary Space: O(N)

Constraints:
1<= N <= 104

'''

class Solution:
    def sieveOfEratosthenes(self, N):
        primes=[i for i in range(2,N+1)]   #Assume all numbers are prime
              #[2,3,4,5,6,7,8,9,10]        #say N=10
        for i in range(len(primes)):       #for each number cancel out its multiples
            if primes[i]!=-1:              #check if number is already cancelled
                j=i                        
                while j+primes[i]<len(primes):
                  j+=primes[i]
                  primes[j]=-1
        return [i for i in primes if i!=-1]
