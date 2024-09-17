"""
leetcode.com/problem-list/string/
https://leetcode.com/problems/regular-expression-matching/description/
"""

class Solution(object):
    def isMatch(self, s, p):
        pointer=0
        for i in range(len(s)):
            if p[pointer]==s[i]:
                pointer+=1
            elif p[pointer]==".":
                pointer+=1
            elif p[pointer]=="*":
                if s[i]==p[pointer-1] or p[pointer-1]==".":
                    pass
                elif s[i]!=p[pointer-1] and (p[pointer+1]=="." or p[pointer+1]==s[i]):
                    pointer+=2
            elif p[pointer]!=s[i] and pointer<len(p)-1 and p[pointer+1]=="*":
                pointer+=2
                i-=1
            else:
                return False
            if(pointer>len(p)-1):
                return False
        return True
