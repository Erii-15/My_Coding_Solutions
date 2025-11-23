class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        for x in nums:
            if(x%3!=0): #check how many not div by 3, that means it would need 1 operation 
                  #to be div by 3
                count+=1
        return count

        