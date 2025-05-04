class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = maxc = 0
        for i in nums:
            if i == 1:
                count += 1
                maxc = max(maxc, count)
            else:
                count = 0
        return maxc
        