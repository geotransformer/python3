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
    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode()
        total_tail_node = res

        first = l1
        second = l2
        carry = 0
        # Termination condition - all is None
        while first or second or carry:
            # Do the sum
            digit_sum = carry
            if first is not None:
                digit_sum += first.val
                first = first.next
            if second is not None:
                digit_sum += second.val
                second = second.next

            if digit_sum > 9:
                carry = digit_sum // 10
                digit_sum = digit_sum % 10
            else:
                carry = 0

            # update the tail node pointer
            total_tail_node.next = ListNode(digit_sum)
            total_tail_node = total_tail_node.next

        return res.next


print(12//10)