class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = str(s)
        result, i = 0, 0
        num = {
            "CM":900,
            "CD":400,
            "M":1000,
            "D":500,
            "XC":90,
            "XL":40,
            "C":100,
            "L":50,
            "IX":9,
            "IV":4,
            "X":10,
            "V":5,
            "I":1
        }
        while i < len(s):
            if i + 1 < len(s) and s[i:i+2] in num:
                result += num[s[i:i+2]]
                i +=2
            else:
                result += num[s[i]]
                i +=1
        return result