class Solution {
    public int rob(int[] nums) {
        int prev=0,curr=0;
        int temp;
        for(int i:nums){
            temp=prev;
            prev=curr;
            curr=Math.max((temp+i),prev);
        }
        return curr;
    }
}
