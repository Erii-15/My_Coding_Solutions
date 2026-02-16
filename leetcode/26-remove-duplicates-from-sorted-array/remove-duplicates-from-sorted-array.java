class Solution {
    public int removeDuplicates(int[] nums) {
        int uniqueIndex=0;
        for(int x=0;x<nums.length;x++){
            if (nums[x]!=nums[uniqueIndex]){
                uniqueIndex++;
                nums[uniqueIndex]=nums[x];
            }
        }
        return uniqueIndex+1;
    }
}