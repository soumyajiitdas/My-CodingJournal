class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ## method 1:
        # exp_sum = n*(n+1)//2
        # actual_sum = sum(nums)
        # return exp_sum - actual_sum

        ## method 2:
        xor1 = xor2 = 0
        for i in range(n):
            xor1 ^= i              # calculates xor from 0 to n-1
            xor2 ^= nums[i]        # calculates xor of every elements in nums
        xor1 ^= n                  # calculates xor of xor1 and n (to get xor from 0 to n)
        return xor1 ^ xor2         # returs the missing num

        