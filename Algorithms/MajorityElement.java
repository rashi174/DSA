/*
   Majority Element

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-231 <= nums[i] <= 231 - 1
 

Follow-up: Could you solve the problem in linear time and in O(1) space?

*/

/*
Approach

If we had some way of counting instances of the majority element as +1+1 and instances of any other element as -1−1, 
summing them would make it obvious that the majority element is indeed the majority element.

>> Boyer-Moore Voting Algorithm

1. Mark 1st elemnt as majority elemnt.
2. Keep updating count by 1 everytime you see majority element repeating
3. If element is different then decrement the count by 1
4. Keep checking if count is 0 than update majority element as current element.

:) Time complexity : O(n)O(n)

Boyer-Moore performs constant work exactly nn times, so the algorithm runs in linear time.

:) Space complexity : O(1)O(1)

Boyer-Moore allocates only constant additional memory.


*/

class Solution {
    public int majorityElement(int[] a) {
        int count=0; //count of majority element
        int ansIndex=0;
        int size=a.length;
        for(int i=0;i<size;i++){
            if (a[i]==a[ansIndex]){
                count++;
            }
            else{
                count--;
            }
            if (count==0){
                ansIndex=i;
                count++;
            }
        }
        return a[ansIndex];
    }
}
