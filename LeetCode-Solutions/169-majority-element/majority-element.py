class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        target, count = None, 0

        for num in nums:
            if count == 0:
                target = num
            count += (1 if num == target else -1)

        return target
        