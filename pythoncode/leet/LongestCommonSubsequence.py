'''
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none)
deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not).
A common subsequence of two strings is a subsequence that is common to both strings.

If there is no common subsequence, return 0.


Example 1:

Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.
'''


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        prev = [0 for _ in range(m + 1)]
        for i in range(1, n + 1):
            curr = [0]
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    curr.append(prev[j - 1] + 1)
                else:
                    curr.append(max(curr[j - 1], prev[j]))
            prev = curr
        return prev[-1]

