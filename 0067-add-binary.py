# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ret = []
        part_sum = 0
        for i in range(1, max(len(a), len(b)) + 1):
            part_a = 0 if len(a) < i else a[-i] == '1'
            part_b = 0 if len(b) < i else b[-i] == '1'
            sum = part_a + part_b + part_sum
            ret.append(sum % 2)
            part_sum = sum // 2
        return "".join(list(map(str, [1]*part_sum + ret[::-1])))
    
s = Solution()
print(s.addBinary("11", "1"))
print(s.addBinary("1010", "1011"))

