'''
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
'''
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        for i in nums:
            if nums.count(i) == 1:
                return i
        '''

        '''
        return (int((3 * sum(set(nums)) - sum(nums)) / 2))
        '''

        a = b = 0
        for n in nums:
            b = b ^ n & ~a
            a = a ^ n & ~b
        return a | b


num = [4,4,4,1,78,2,2,1,2,1]

s = Solution()

print(s.singleNumber(num))