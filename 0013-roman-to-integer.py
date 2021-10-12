# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        number = { 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900,
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ret = 0
        pos = 0
        while pos < len(s):
            for key in number.keys():
                if s[pos:].startswith(key):
                    ret += number[key]
                    pos += len(key)
                    break
        return ret
    
s = Solution()
print(s.romanToInt('MCMLXXIX'))
        
            