class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hash_dict = {}
        for i in nums:
            if i in hash_dict:
                hash_dict[i] += 1
            else:
                hash_dict[i] = 1
            if hash_dict[i] > 1:
                return True
        return False
        