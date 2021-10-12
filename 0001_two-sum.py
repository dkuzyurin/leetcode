# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_sorted = sorted(nums)
        for ind in range(len(nums_sorted)):
            a = nums_sorted[ind]
            b = target - a
            if b in nums_sorted[ind+1:]:
                ind_a = nums.index(a)
                ind_b = nums.index(b)
                if ind_a == ind_b:
                    ind_b = nums.index(b, ind_a + 1)
                return [ind_a, ind_b]
            

s = Solution()
print(s.twoSum([-1,-2,-3,-4,-5], -8))
            
            
        