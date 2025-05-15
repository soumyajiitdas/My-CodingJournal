class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        hash_dict = {}
        j = mlen = 0
        for i in range(n):
            if s[i] in hash_dict:
                j = max(j, hash_dict[s[i]] + 1)
                hash_dict[s[i]] = i

            hash_dict[s[i]] = i
            mlen = max(mlen, i-j+1)
        return mlen

        