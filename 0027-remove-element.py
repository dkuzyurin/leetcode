# https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cur_ind = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[cur_ind] = nums[i]
                cur_ind += 1
        return cur_ind
                

s = Solution()
x = [0,1,2,2,3,0,4,2]
print(s.removeElement(x, 2), x)