class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        even = 0
        odd = n-1

        while even < odd:
            if nums[even] % 2 == 1:
                nums[even], nums[odd] = nums[odd], nums[even]
                odd -= 1
            else:
                even += 1
        
        return nums


        