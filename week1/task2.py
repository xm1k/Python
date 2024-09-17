"""
leetcode.com/problem-list/string/
https://leetcode.com/problems/longest-palindromic-substring/description/
"""

class Solution(object):
    def longestPalindrome(self, s):
        p1 = 0
        p2 = 0
        for i in range(len(s)):
            for j in range(len(s)-1, i, -1):
                if(s[i] == s[j]):
                    p1=i
                    p2=j
                    while(True):
                        if s[p1]==s[p2]:
                            if p2 <= p1:
                                return(s[i:j+1])
                            p1 += 1
                            p2 -= 1
                        else:
                            break
        return("")
