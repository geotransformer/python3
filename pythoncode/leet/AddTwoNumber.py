'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: object = None) -> object:
        self.val = val
        self.next = next


class Solution:
    def add_two_numbers(self, l1: ListNode, l2: ListNode, carry: int = 0) -> ListNode:
        # Termination
        if l1 is None and l2 is None:
            return None if carry == 0 else ListNode(carry)

        res = ListNode(carry)

        if l1 is not None:
            res.val += l1.val
        else:
            l1 = ListNode(0)

        if l2 is not None:
            res.val += l2.val
        else:
            l2 = ListNode(0)

        carry = res.val // 10
        res.val = res.val % 10

        res.next = self.add_two_numbers(l1.next, l2.next, carry)

        return res
