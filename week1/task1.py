"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        symbols=[]
        mx=0
        cur=0
        for i in range(len(s)):
            if s[i] not in symbols:
                symbols.append(s[i])
                cur+=1
            else:
                if cur>mx:
                    mx=cur
                symbols=[]
                symbols.append(s[i])
                cur=1
        if cur>mx:
            mx=cur
        return(mx)

