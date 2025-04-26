# Last updated: 4/26/2025, 12:33:57 PM
class Solution(object):
    def romanToInt(self, s):
        roman_val = {
        'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000
        }
        total = 0
        pre_val = 0
        
        for i in reversed(s):
            val = roman_val[i]
            if val < pre_val:
                total -= val
            else:
                total += val
            pre_val = val
        return total
