# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        sym_ind = 0
        while sym_ind < len(strs[0]):
            sym = strs[0][sym_ind]
            for str_num in range(1, len(strs)):
                if len(strs[str_num]) <= sym_ind \
                    or strs[str_num][sym_ind] != sym:
                        return prefix
            prefix += sym
            sym_ind += 1
        return prefix
    
s = Solution()
print(s.longestCommonPrefix(["","",""]))
            