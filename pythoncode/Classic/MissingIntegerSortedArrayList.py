'''
You are given a sorted list of distinct integers from 0 to 99,
for instance [0, 1, 2, 4, 50, 52, 75].
Your task is to produce a string that describes numbers missing from the list;
in this case "3,5-49,51,53-74,76-99". The items should be sorted in ascending order
and separated by commas when a gap spans only one number. When a gap is longer,
the item comprises the start and the end of the gap, joined with a minus sign.
'''
from typing import List

class Solution:
    def listMissingIntegers(self, nums: List[int]) -> str:
        res = ""
        i = 1
        # the beginning
        if nums[0] != 0:
            res = res + str(0) + ","

        while i < len(nums):
            if nums[i] - nums[i - 1] == 2:
                res = res + str((nums[i - 1] + 1)) + ","
            elif nums[i] - nums[i - 1] > 2:
                res = res + str((nums[i - 1] + 1)) + "-" + str((nums[i] - 1)) + ","
            i += 1

        # the ending
        if nums[i - 1] != 99:
            if 99 - nums[i - 1] == 2:
                res = res + str((nums[i - 1] + 1)) + ","
            elif 99 - nums[i - 1] > 2:
                res = res + str((nums[i - 1] + 1)) + "-"
            res = res + str(99)
        else:
            res = res[:-1]

        return res

s = Solution()
nums = [1, 2, 4, 50, 52, 75, 97, 98, 99]
print(s.listMissingIntegers(nums))