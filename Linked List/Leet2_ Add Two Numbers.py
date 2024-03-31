2. Add Two Numbers
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        root = n = ListNode(0)          #tạo ra node đầu tiên trong linked list có giá trị  = 0
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:                      #xét khác None không
                v1 = l1.val
                l1 = l1.next
            if l2:                      #xét khác None không
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1 + v2 + carry, 10)    #divmod(x, y) trả về một bộ gồm hai giá trị: phần nguyên của phép chia x cho y và phần dư của phép chia đó.
                                                        # carry = phần nguyên của (v1 + v2 + carry) /10 ; val = phần dư
            n.next = ListNode(val)      #tạo node đầu tiên của list result
            n = n.next
        return root.next                #Bỏ qua node 0 lúc khởi tạo ban đầu