# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums) -> int:
        sum_max = nums[0]
        sum_cur = 0
        for i in range(len(nums)):
            sum_cur = nums[i] + sum_cur * int((sum_cur + nums[i]) > nums[i])
            if sum_cur > sum_max:
                sum_max = sum_cur
        return sum_max
    
s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

        