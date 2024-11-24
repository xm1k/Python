"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/subarray-product-less-than-k/description/
"""


class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0
        for p1 in range(len(nums)):
            cur = 1
            cur_ar = []
            for p2 in range (p1, len(nums)):
                cur *= nums[p2]
                cur_ar.append(nums[p2])
                if(cur < k):
                    ans += 1
                else:
                    break
        return ans