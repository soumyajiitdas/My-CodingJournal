class Solution(object):
    def lengthOfLastWord(self, s):
        string = s.rstrip()
        
        length = 0
        i = len(string) - 1

        while i >= 0 and string[i] != " ":
            length += 1
            i -= 1
        return length 
        