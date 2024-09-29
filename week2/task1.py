"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/integer-to-roman/description/
"""

class Solution(object):
    def intToRoman(self, num):
        romans = [ (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I') ]

        roman_str = ''

        for value, symbol in romans:
            while num >= value:
                roman_str += symbol
                num -= value

        return roman_str
