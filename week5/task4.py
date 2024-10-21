"""
https://leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
"""

class Solution(object):
    def findSubstring(self, s, words):
        res = []
        l1 = len(words[0])
        lw = len(words)
        l = l1 * lw
        words_c = ''.join(sorted(words))
        for i in range(len(s) - l + 1):
            subs = ''.join(sorted([s[i+j*l1:i+j*l1+l1] for j in range(lw)]))
            if subs == words_c:
                res.append(i)

        return res