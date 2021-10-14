# https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums, target) -> int:
        start = 0
        right_bound = end = len(nums) - 1
        while start <= end:
            cur = (end - start) // 2 + start
            if nums[cur] == target:
                    return cur
            if nums[cur] > target:
                right_bound = cur
                end = cur - 1
            else:
                start = cur + 1
        return right_bound + int(nums[right_bound] <= target)
            
    
s = Solution()
print(s.searchInsert([1,3,5,6], 5))
print(s.searchInsert([1,3,5,6], 2))
print(s.searchInsert([1,3,5,6], 7))
print(s.searchInsert([1,3,5,6], 0))
        
        