class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y = str(x)
        z = y[::-1]
        for i in range(len(y)):
            if z[i] != y[i]:
                return False
        return True