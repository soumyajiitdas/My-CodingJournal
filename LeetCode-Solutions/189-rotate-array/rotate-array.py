class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # Handle d > n
        if k == 0:
            return
        nums[n-k:] = nums[n-k:][::-1]
        nums[:n-k] = nums[:n-k][::-1]
        nums[:] = nums[:][::-1]
        