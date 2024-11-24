"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/repeated-dna-sequences/description/
"""
from numpy.ma.core import array


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        voc = {}
        for i in range(len(s)-9):
            if(s[i:i+10] not in voc):
                voc[s[i:i+10]] = 1
            else:
                voc[s[i:i + 10]] += 1
        res = []
        for el in voc:
            if voc[el] >= 2:
                res.append(el)
        return res