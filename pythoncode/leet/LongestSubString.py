'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
'''
class Solution:
    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:
        if s is None or len(s) == 0:
            return 0

        current = ""
        temp = ""
        for i in range(len(s)):
            if s[i] not in temp:
                temp += s[i]
            else:
                if len(current) < len(temp):
                    current = temp
                temp = temp[temp.index(s[i]) + 1:] + s[i]

        return max(len(current), len(temp))


print(Solution.lengthOfLongestSubstring("pw3wkew"))
