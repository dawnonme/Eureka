class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        sx = str(x)
        rsx = sx[::-1]
        return sx == rsx
