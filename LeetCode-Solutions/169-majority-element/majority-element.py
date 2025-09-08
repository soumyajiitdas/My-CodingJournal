class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        hash_dict = {}

        for i in range(n):
            if nums[i] in hash_dict:
                hash_dict[nums[i]] += 1
            else:
                hash_dict[nums[i]] = 1
        
        for i in hash_dict:
            if hash_dict[i] > n//2:
                return i
        