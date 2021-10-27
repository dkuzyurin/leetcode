# https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        point_1 = point_2 = 0
        point_1_end = m
        while point_1 < (m+n) and point_2 < n:
            while point_1 < point_1_end and nums1[point_1] <= nums2[point_2]:
                point_1 += 1
            for i in range(point_1_end, point_1, -1):
                nums1[i] = nums1[i-1]
            nums1[point_1] = nums2[point_2]
            point_1_end += 1
            point_2 += 1
                
    
s = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
s.merge(nums1, m, nums2, n)
print(nums1)

nums1 = [0]
m = 0
nums2 = [1]
n = 1
s.merge(nums1, m, nums2, n)
print(nums1)

nums1 = [1]
m = 1
nums2 = []
n = 0
s.merge(nums1, m, nums2, n)
print(nums1)