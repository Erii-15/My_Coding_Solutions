class Solution(object):
    def lengthOfLastWord(self, s):
        words=s.split()
        num=0
        for x in words:
           num=len(x)
        return num
        