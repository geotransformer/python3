'''
Given an array of integers arr, write a function that returns true if and
only if the number of occurrences of each value in the array is unique.

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
'''


from typing import List

class Solution:
    def uniqueOccurrences(arr: List[int]) -> bool:
        '''
        occ_map = {}
        for n in arr:
            occ_map[n] = occ_map.get(n, 0) + 1

        lst = list(occ_map.values())
        lst.sort()

        for i in range(len(lst)-1):
            if lst[i] == lst[i + 1]:
                return False
            else:
                i += 1
        return True
        '''
        result = {}
        for n in arr:
            if n not in result:
                result[n] = arr.count(n)
        result_list = result.values()
        return len(result_list) == len(set(result_list))

arr = [1,2,2,1,1,3]
print(Solution.uniqueOccurrences(arr))


