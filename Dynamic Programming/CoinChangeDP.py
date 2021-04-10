'''
https://leetcode.com/problems/coin-change/

322. Coin Change

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
Example 4:

Input: coins = [1], amount = 1
Output: 1
Example 5:

Input: coins = [1], amount = 2
Output: 2
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104

'''

#DP approach
class Solution:
    def coinChange(self, coins: List[int], rupee: int) -> int:
        dp=[-1]*(rupee+1) 
        dp[0]=0
        result=self.mincoins(rupee,coins,dp)
        if result==float('inf'):
            return -1
        return result
        
    
    def mincoins(self,n,arr,dp):
        if n==0:
            return 0
        ans=float('inf')
        for i in range(len(arr)):
            if (n-arr[i]>=0):
                if (dp[n-arr[i]]!=-1):
                    subans=dp[n-arr[i]]
                else:
                    subans=self.mincoins(n-arr[i],arr,dp)
                if subans!=float('inf') and subans+1 < ans:
                    ans=subans+1
        dp[n]=ans
        return dp[n]
                    
