"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/permutation-in-string/description/
"""


def get_voc(s):
    voc = {}
    for i in s:
        if i not in voc:
            voc[i] = 1
        else:
            voc[i] += 1

class Solution(object):
    def checkInclusion(self, s1, s2):
        p_voc = {}
        voc = {}
        for i in range(len(s1)):
            if s2[i] not in voc:
                voc[s2[i]] = 1
            else:
                voc[s2[i]] += 1
            if s1[i] not in p_voc:
                p_voc[s1[i]] = 1
            else:
                p_voc[s1[i]] += 1
        if voc == p_voc:
            return True
        for i in range(len(s2)-len(s1)):
            voc[s2[i]] -= 1
            if(voc[s2[i]] == 0):
                del voc[s2[i]]
            if s2[i+len(s1)] not in voc:
                voc[s2[i + len(s1)]] = 1
            else:
                voc[s2[i + len(s1)]] += 1
            if(p_voc == voc):
                return True
        return False
