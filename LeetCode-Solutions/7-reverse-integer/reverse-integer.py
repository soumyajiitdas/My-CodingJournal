class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        sign = -1 if x < 0 else 1
        x = abs(x)

        rev_digit = 0
        while x != 0:
            last_digit = x % 10
            x = x // 10

            if rev_digit > (INT_MAX - last_digit) // 10 :
                return 0

            rev_digit = rev_digit * 10 + last_digit
        
        return sign * rev_digit