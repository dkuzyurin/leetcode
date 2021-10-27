# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def __init__(self):
        self.stairs = {}
    def climbStairs(self, n: int) -> int:
        if n not in self.stairs:
            self.stairs[n] = n if n <= 3 \
                else self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.stairs[n]
    
s = Solution()
for n in [3, 4, 5, 30, 35, 40, 45]:
    print(n, s.climbStairs(n))

