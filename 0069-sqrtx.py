# https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        max_possible_rt = 2 ** 16 # 65536
        min_rt = 0
        max_rt = max_possible_rt
        max_rt = 2 ** 16 # 65536
        while max_rt >= 0 and min_rt <= max_possible_rt \
                and min_rt < max_rt - 1:
            mean_rt = int((max_rt - min_rt) / 2 + min_rt)
            if mean_rt ** 2 == x:
                return mean_rt
            if mean_rt ** 2 < x:
                min_rt = mean_rt
            else:
                max_rt = mean_rt
        return min_rt
    
s = Solution()
for num in [0, 1, 2, 3, 4, 5, 9, 12, 16, 20, 25, 30]:
    print(num, s.mySqrt(num))
            
            