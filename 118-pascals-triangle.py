# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = [[1]]
        for row in range(numRows-1):
            new_row = []
            for i in range(len(ret[row]) + 1):
                new_el = ret[row][i-1] + ret[row][i] \
                    if (i > 0 and i < len(ret[row])) else 1
                new_row.append(new_el)
            ret.append(new_row)
        return ret
                
            

s = Solution()
print(s.generate(1))
print(s.generate(5))

