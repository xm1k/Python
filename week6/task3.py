"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/minimum-size-subarray-sum/description/
"""

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        minimum = 0
        p1 = 0
        for p1 in range(len(nums)):
            sum = 0
            for p2 in range(p1,len(nums)):
                sum+=nums[p2]
                if sum>=target:
                    if(minimum == 0):
                        minimum = p2-p1+1
                    else:
                        minimum = min(minimum, p2-p1+1)
                    break
        return minimum
