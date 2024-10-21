"""
https://leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        start = 0
        end = 0
        substring = ""
        length = 0

        while (end < len(s)):
            while (start < end and s[end] in substring):
                start += 1
                substring = s[start:end]

            substring += s[end]
            length = max(length, len(substring))
            end += 1

        return (length)