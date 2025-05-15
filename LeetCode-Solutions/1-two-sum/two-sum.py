class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        preSum = {}
        for i in range(n):
            rem = target - nums[i]
            if rem in preSum:
                return preSum[rem], i
            preSum[nums[i]] = i
        
        