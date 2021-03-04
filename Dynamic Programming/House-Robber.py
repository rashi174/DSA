'''
198. House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 400

'''


# Approach 1 - Using Memoization 
# Time- O(N)   Space- O(N)

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        
        memo=[0]*len(nums)
        memo[0]=nums[0]
        memo[1]=max(nums[1],nums[0])
        
        for i in range(2,len(nums)):
            memo[i]=max(memo[i-2]+nums[i],memo[i-1])
        return max(memo)

# Approach 2 
# Time- O(N) Space- O(1)

class Solution:
    def rob(self, nums: List[int]) -> int:
        prev=0
        curr=0
        for num in nums:
            temp=prev
            prev=curr
            curr=max((temp+num),prev)
        return curr
      
  '''
                                Explanation
  
At each house there are two options: either to rob it or not to rob it.

Option 1: If rob, then rob = not_rob + nums[i]
(max money if rob the current house = max money if not rob the last house + amount of the current house)

Option 2: If not rob, then not_rob = max(rob, not_rob)
(max money if not rob the current house = max money at the last house, either rob or not rob)
  
  '''
        
        
        
