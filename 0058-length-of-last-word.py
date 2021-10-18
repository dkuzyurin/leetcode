# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ind = 0
        while s[::-1][ind] == ' ':
            ind += 1
        first = ind
        while ind < len(s) and s[::-1][ind] != ' ':
            ind += 1
        return ind - first
    
s = Solution()
print(s.lengthOfLastWord("   fly me   to   the moon  "))
            