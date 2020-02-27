# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ptr = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            print(carry)
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            ptr.next = ListNode(carry % 10)
            ptr = ptr.next
            carry //= 10
        return dummy.next


a = ListNode(2)
a.next = ListNode(9)
a.next.next = ListNode(9)

d = ListNode(9)
d.next = ListNode(9)
d.next.next = ListNode(9)
sol = Solution()
q = sol.addTwoNumbers(a, d)

while q:
    print(q.val)
    q = q.next
