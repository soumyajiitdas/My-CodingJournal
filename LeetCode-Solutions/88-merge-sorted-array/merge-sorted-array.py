class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        temp = nums1[:m] + nums2[:n]
        left, right = 0, m
        nums1[:] = []
        while left < m and right < m+n:
            if temp[left] <= temp[right]:
                nums1.append(temp[left])
                left += 1
            else:
                nums1.append(temp[right])
                right += 1
        
        while left < m:
            nums1.append(temp[left])
            left += 1
        
        while right < m+n:
            nums1.append(temp[right])
            right += 1