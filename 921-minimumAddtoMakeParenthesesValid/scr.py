class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        open_parentheses = 0
        res = 0

        for char in s:
            if char == '(':
                open_parentheses += 1
            else:
                open_parentheses -=1
                if open_parentheses < 0:
                    open_parentheses = 0
                    res += 1

        return open_parentheses + res

        