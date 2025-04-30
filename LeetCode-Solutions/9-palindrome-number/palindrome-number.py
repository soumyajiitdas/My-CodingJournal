class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        rev_num_half = 0
        while x > rev_num_half:
            rev_num_half = rev_num_half * 10 + (x % 10)
            x = x // 10

        return x == rev_num_half or x == rev_num_half // 10
