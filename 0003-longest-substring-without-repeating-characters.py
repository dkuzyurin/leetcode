# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        for i in range(len(s)):
            j = 1
            while (i+j) < len(s) and s[i+j] not in s[i:i+j]:
                j += 1
            max_len = max(max_len, j)
        return max_len

s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
            