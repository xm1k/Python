"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/find-k-closest-elements/description/
"""


class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        ans = []
        # isEven = (k%2 == 0)
        # if isEven: k-=1
        # pivot = (k-1)/2
        true_piv = 0
        mn = x
        for i, c in enumerate(arr):
            if abs(c - x)<mn:
                mn = abs(c - x)
                true_piv = i
        ans.append(arr[true_piv])
        k -= 1
        p1 = true_piv
        p2 = true_piv
        while(k>0):
            if (p1 > 0):
                if(p2 < len(arr)):
                    if(abs(arr[p1-1]-x) < abs(arr[p2+1]-x) or (abs(arr[p1-1]-x) == abs(arr[p2+1]-x) and p1<p2)):
                        p1 -= 1
                        ans.insert(0, arr[p1])
                        k -= 1
                    else:
                        p2 += 1
                        ans.append(arr[p2])
                        k-=1
                else:
                    p1 -= 1
                    ans.insert(0, arr[p1])
                    k-=1
            elif (p2 < len(arr)):
                p2 += 1
                ans.append(arr[p2])
                k -= 1
            else:
                break
        return ans
