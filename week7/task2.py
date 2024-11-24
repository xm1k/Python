"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/longest-repeating-character-replacement/description/
"""

def find_max(voc):
    count=0
    mx = 0
    mxx = ''
    for v in voc:
        count+=voc[v]
        if voc[v] > mx:
            mx = voc[v]
            mxx = v
    if(mxx!=''):
        count-=voc[mxx]
    return count, mxx

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        mx = 0
        for p1 in range(len(s)):
            voc = {}
            for p2 in range(p1, len(s)):
                k_c, k_v = find_max(voc)
                if s[p2] not in voc and k_c<k:
                    voc[s[p2]] = 1
                elif k_v == s[p2] or k_c<k:
                    voc[s[p2]] += 1
                else:
                    break
                mx = max(mx,p2-p1+1)
        return mx
