class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if not -2**31 <= x <= 2**31 - 1:
            return False
        x = str(x)
        rev = x[::-1]
        if x == rev:
            return True
        else:
            return False
