class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n<=0): return False
        while(n%2==0):
            n=n//2 #if just use / it will return a float
        
        return n==1 # After dividing out all 2s, if we reach 1, it was a power of 2
        