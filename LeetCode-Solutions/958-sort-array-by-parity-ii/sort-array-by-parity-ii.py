class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        even = 0
        odd = 1
        while odd < n and even < n:
            if nums[odd] % 2 == 0:
                nums[even], nums[odd] = nums[odd], nums[even]
                even += 2
            else:
                odd += 2
        
        return nums

