# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        coord = []
        go_down = 1
        x = y = 0
        for ind in range(len(s)):
            coord.append((x, y, s[ind]))  # [(x, y, symbol)]
            if go_down:
                x += 1
                if x == numRows - 1:
                    go_down = 0
            else:
                x -= 1
                y += 1
                if not x:
                    go_down = 1
        coord.sort(key = lambda x: x[0])
        return "".join(list(map(lambda x: x[2], coord)))
                 
s = Solution()
print(s.convert("PAYPALISHIRING", 1))
print(s.convert("PAYPALISHIRING", 3))
print(s.convert("PAYPALISHIRING", 4))

