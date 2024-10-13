"""
leetcode.com/problem-list/array/
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
"""


class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k
