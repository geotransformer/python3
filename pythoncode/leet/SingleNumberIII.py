'''
Given an array of numbers nums, in which exactly two elements appear only once
and all the other elements appear exactly twice.
Find the two elements that appear only once.

Example:

Input:  [1,2,1,3,2,5]
Output: [3,5]

1, The order of the result is not important. So in the above example, [5, 3] is also correct.
2, Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

'''
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        '''
        val = 0
        for i in nums:
            val ^= i
        for i in nums:
            if val ^ i in nums:
                return [i, val ^ i]
        '''

        unique_set = set()
        for num in nums:
            if len(unique_set & set([num])):
                unique_set.remove(num)
            else:
                unique_set.add(num)
        return list(unique_set)


n = [1, 2, 1, 3, 2, 5]
s = Solution()
print(s.singleNumber(n))
