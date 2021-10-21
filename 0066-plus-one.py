# https://leetcode.com/problems/plus-one/

class Solution:   
    def plusOne(self, digits: List[int]) -> List[int]:
        to_add = 1
        ret = digits.copy()
        i = 1
        while to_add and i <= len(digits):
            if ret[-i] == 9:
                ret[-i] = 0
            else:
                ret[-i] += 1
                to_add = 0
            i += 1
        return [1] * to_add + ret
    
s = Solution()
print(s.plusOne([4, 3, 2, 1]))
print(s.plusOne([4, 5, 9]))
print(s.plusOne([9, 9]))
print(s.plusOne([9]))
            

