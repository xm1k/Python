"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/count-and-say/description/
"""
class Solution:
    def countAndSay(self, n):
        if n == 1:
            return "1"
        previous_say = self.countAndSay(n - 1)
        result = []
        count = 1
        for i in range(1, len(previous_say)):
            if previous_say[i] == previous_say[i - 1]:
                count += 1
            else:
                result.append(str(count))
                result.append(previous_say[i - 1])
                count = 1
        result.append(str(count))
        result.append(previous_say[-1])
        return ''.join(result)