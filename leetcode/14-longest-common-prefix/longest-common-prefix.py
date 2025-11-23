class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix=strs[0]

        while not all(s.startswith(prefix) for s in strs) and prefix!="":
            prefix=prefix[:-1] #removes last letter
            
        return prefix

        