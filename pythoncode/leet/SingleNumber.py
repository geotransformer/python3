'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
'''
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        occ_map = {}
        for n in nums:
            occ_map[n] = occ_map.get(n, 0) + 1

        for k, v in occ_map.items():
            if v == 1:
                return k
        '''
        m = 0
        for n in nums:
            m ^= n
        return m


num = [4,4,1,7,7,2,1,2]

s = Solution()

print(s.singleNumber(num))