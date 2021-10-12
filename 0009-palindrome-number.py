# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x_digits = []
        while x > 0:
            x_digits.append(x % 10)
            x //= 10
        x_len = len(x_digits)
        for i in range(x_len // 2):
            if x_digits[i] != x_digits[x_len-i-1]:
                return False
        return True
        
        
s = Solution()
print(s.isPalindrome(13431))
