"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/
"""


class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        mx = 0
        for p1 in range(len(s)):
            voc = {}
            for p2 in range(p1,len(s)):
                if(s[p2] not in voc):
                    voc[s[p2]] = 1
                else:
                    voc[s[p2]] += 1

                for l in voc:
                    if(voc[l]<k):
                        break
                else:
                    mx = max(mx, p2-p1+1)
                    continue
        return mx
