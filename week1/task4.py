"""
leetcode.com/problem-list/string/
https://leetcode.com/problems/string-to-integer-atoi/description/
"""

class Solution(object):
    def myAtoi(self, s):
        sign=1
        flag=0
        while s[0] == " ":
            s = s[1:]
        if s[0]=="-":
            sign=-1
            s=s[1:]
        for i in range(len(s)):
            while s[i]==" ":
                s=s[:i]+s[i+1:]
            if s[i].isdigit()==False:
                if not flag:
                    return 0
                else:
                    num = int(s[:i])
                    return num*sign
            else:
                flag=1
        return int(s)*sign