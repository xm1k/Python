"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/median-of-two-sorted-arrays/description/
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total_len = m + n
        half_len = total_len // 2
        left, right = 0, m

        while left <= right:
            i = (left + right) // 2
            j = half_len - i

            nums1_left = nums1[i - 1] if i > 0 else float('-inf')
            nums1_right = nums1[i] if i < m else float('inf')
            nums2_left = nums2[j - 1] if j > 0 else float('-inf')
            nums2_right = nums2[j] if j < n else float('inf')

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if total_len % 2:
                    return float(min(nums1_right, nums2_right))
                return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2.0
            elif nums1_left > nums2_right:
                right = i - 1
            else:
                left = i + 1