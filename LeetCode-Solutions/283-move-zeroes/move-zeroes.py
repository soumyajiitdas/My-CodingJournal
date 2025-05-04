class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums) 
        i = 0
        for j in range(n):
            if nums[j] == 0:
                i = j
                break
        
        for j in range(i+1, n):
            if nums[j] != 0 and nums[i] == 0:           # avoids unecessary swappings
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        