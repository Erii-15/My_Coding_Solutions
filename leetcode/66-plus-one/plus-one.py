class Solution(object):
    def plusOne(self, digits):
        n = len(digits)
        
        # Start from the last digit, stops at 0 in increments on -1
        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0  # carry over

        # If all digits were 9, we need an extra 1 at the beginning
        return [1] + digits
        