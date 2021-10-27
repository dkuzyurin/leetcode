# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        signum = 1 if x >=0 else -1
        while x:
            rev = 10 * rev + (abs(x) % 10)
            x = abs(x) // 10
        return rev* signum if -(2**31) - 1 < rev < 2**31 else 0
    
s = Solution()
for x in [0, 123, -321, -3246, 20000, -5100, 1534236469]:
    print(x, s.reverse(x))
            
        

