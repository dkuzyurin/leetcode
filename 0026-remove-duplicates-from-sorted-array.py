# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current_count = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[current_count - 1]:
                nums[current_count] = nums[i]
                current_count += 1
        return current_count
    
s = Solution()
x = [0,0,1,1,1,2,2,3,3,4]
print(s.removeDuplicates(x), x)
            