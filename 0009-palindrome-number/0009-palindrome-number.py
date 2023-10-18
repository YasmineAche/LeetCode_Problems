class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        y = x[::-1]
        for i in range(len(x)):
            if x[i] != y[i]:
                return False
        return True