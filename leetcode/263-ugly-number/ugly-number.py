class Solution(object):
    def isUgly(self, n):
        if n <= 0:
            return False
        for f in [2, 3, 5]:
            while n % f == 0:
                n //= f #floor division
        return n==1
        