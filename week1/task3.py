"""
leetcode.com/problem-list/string/
https://leetcode.com/problems/zigzag-conversion/description/
"""

class Solution(object):
    def convert(self, s, numRows):
        matrix=[[]*numRows for _ in range(numRows)]
        cur=0
        state=1
        for i in range(len(s)):
            matrix[cur].append(s[i])
            if state==1:
                cur+=1
            else:
                cur-=1
            if cur==numRows or cur==-1:
                state=-state
                cur+=state*2
        string = ""
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                string += matrix[i][j]
        return string