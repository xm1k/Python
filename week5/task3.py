"""
https://leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
"""

from itertools import product
class Solution(object):
    def letterCombinations(self, digits):
        l=[]
        if len(digits)==0:
            return l
        d={
            2:"abc",
            3:"def",
            4:"ghi",
            5:"jkl",
            6:"mno",
            7:"pqrs",
            8:"tuv",
            9:"wxyz"
        }
        for i in digits:
            l.append(d[int(i)])
        combinations = [''.join(triplet) for triplet in product(*l)]
        return combinations