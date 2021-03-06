'''
Given a sorted array nums, remove the duplicates in-place
such that each element appear only once and return the new length.

Do not allocate extra space for another array,
you must do this by modifying the input array in-place with O(1) extra memory.

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements
of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
'''

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        i = 1
        j = 0
        while i < n:
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
            i += 1
        return j + 1

s = Solution()

nums = [0,0,1,1,1,2,2,3,3,4, 4, 4]

print(s.removeDuplicates(nums))
print(nums[0:5])







