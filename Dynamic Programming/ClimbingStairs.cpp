/*
Count ways to reach the n'th stair 

There are N stairs, a person standing at the bottom wants to reach the top. The person can climb either 1 stair or 2 stairs at a time. Count the number of ways, the person can reach the top (order does matter).

Example 1:

Input:
N = 4
Output: 5
Explanation: You can reach 4th stair in
5 ways.
Example 2:

Input:
N = 10
Output: 89
Your Task:
Complete the function countWays() which takes the top stair number m as input parameters and returns the answer % 10^9+7.

Expected Time Complexity : O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 <= N <= 105
*/

/*

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
*/

// function to count ways to reach mth stair
long long countWays(int m){
    if (m==1) return 1;
    if(m==2) return 2;
    return countWays(m-1)+countWays(m-2);
}
