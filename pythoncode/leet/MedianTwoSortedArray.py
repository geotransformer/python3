'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''

from typing import List

class Solution:
    @staticmethod
    def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
        i = 0
        j = 0
        k = 0
        alist = nums1 + nums2

        print(alist)

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                alist[k] = nums1[i]
                i = i + 1
            else:
                alist[k] = nums2[j]
                j = j + 1
            k = k + 1

        while j < len(nums2):
            alist[k] = nums2[j]
            j = j + 1
            k = k + 1

        while i < len(nums1):
            alist[k] = nums1[i]
            i = i + 1
            k = k + 1
        print(alist)
        return alist[k//2] if k % 2 == 1 else (alist[(k-1)//2] + alist[(k+1)//2])/2.0

a = [1, 2, 3, 4, 5,11]
b = [ 6, 7, 8,9, 10]
print(Solution.findMedianSortedArrays(a, b))