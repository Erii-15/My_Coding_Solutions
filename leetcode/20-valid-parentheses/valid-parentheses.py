class Solution(object):
    def isValid(self, s):
        myMap={")":"(","}":"{","]":"["}
        myStack=[]

        for char in s:
            if char in "({[":
                myStack.append(char)
            elif char in ")]}":
                
                if not myStack or myStack.pop()!=myMap[char]:
                    return False
        return not myStack #checks if empty
        