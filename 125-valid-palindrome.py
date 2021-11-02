# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        snew = "".join([ch.lower() for ch in s if ch.isalnum()])
        return snew == snew[::-1]
        
        
s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("race a car"))
print(s.isPalindrome(" "))
print(s.isPalindrome("0P"))