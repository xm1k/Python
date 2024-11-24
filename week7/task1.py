"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
"""


class Solution(object):
    def findAnagrams(self, s, p):
        ans = []
        p_voc={}
        voc = {}
        for i in range(len(p)):
            if p[i] not in p_voc:
                p_voc[p[i]] = 1
            else:
                p_voc[p[i]] += 1

            if s[i] not in voc:
                voc[s[i]] = 1
            else:
                voc[s[i]] += 1

        if p_voc == voc:
            ans.append(0)

        for i in range(len(p),len(s)):
            voc[s[i-len(p)]] -= 1
            if voc[s[i-len(p)]] == 0:
                del voc[s[i-len(p)]]
            if s[i] not in voc:
                voc[s[i]] = 1
            else:
                voc[s[i]] += 1
            if(voc == p_voc):
                ans.append(i-len(p)+1)
        return ans