"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        mx = 0
        for p1 in range(len(s)):
            p2=p1
            cur = set()
            while(p2<len(s) and s[p2] not in cur ):
                cur.add(s[p2])
                p2+=1
            mx = max(mx,p2-p1)
        return mx