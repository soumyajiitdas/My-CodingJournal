class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip()
        length = len(s) - s.rfind(' ') - 1    # rfind(' ') returns last occerence index of ' '

        return length
        