"""
Solution for Longest Palindrome problem
"""
class Solution:
    """
    Method for this problem
    """
    def longest_palindrome_approach_1(self, s: str) -> str:
        if len(s) <= 1:
            return s

        result = s[0]
        result_lenght = 1
        for left in range(len(s) - 1):
            for right in range(left + 1, len(s)):
                if right-left+1 > result_lenght and s[left:right + 1] == s[left:right+1][::-1]:
                    result_lenght = right - left + 1
                    result = s[left:right + 1]
        return result

    def longest_palindrome_approach_2(self, s: str) -> str:

        if len(s) <= 1:
            return s

        def expand_string_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1: right]

        result = s[0]
        for i in range(len(s) - 1):
            odd = expand_string_center(i, i)
            even = expand_string_center(i, i + 1)

            if len(odd) > len(result):
                result = odd
            if len(even) > len(result):
                result = even

        return result

    def longest_palindrome_approach_3(self, s: str) -> str:

        if len(s) <= 1:
            return s
        result = s[0]
        result_lenght = 1

        matrix = [[False for _ in enumerate(s)] for _ in enumerate(s)]
        for i in enumerate(s):
            matrix[i][i] = True
            for j in range(i):
                if s[j] == s[i] and (i - j <= 2 or matrix[j + 1][i - 1]):
                    matrix[j][i] = True
                    if i - j + 1 > result_lenght:
                        result_lenght = i - j + 1
                        result = s[j:i + 1]
        return result
