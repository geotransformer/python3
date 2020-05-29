'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # if the whole string is a palindrome
        if s[::-1] == s:
            return s

        # now for substrings
        for i in range(0, len(s)):
            end_pos = len(s) - (i + 1)
            start_pos = 0
            for j in range(-2, i):
                str_to_check = s[start_pos:end_pos]

                if str_to_check[::-1] == str_to_check:
                    return str_to_check

                start_pos += 1
                end_pos += 1
