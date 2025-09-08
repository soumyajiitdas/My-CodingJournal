class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        cnt = el = 0
        for i in range(n):
            if cnt == 0:
                el = nums[i]
                cnt = 1
            elif nums[i] == el:
                cnt += 1
            else: 
                cnt -= 1
        
        return el

        