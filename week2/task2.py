"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
"""

class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        def backtrack(index, path):
            if len(path) == len(digits):
                combinations.append("".join(path))
                return
            possible_letters = phone_map[digits[index]]
            for letter in possible_letters:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()
        combinations = []
        backtrack(0, [])
        return combinations