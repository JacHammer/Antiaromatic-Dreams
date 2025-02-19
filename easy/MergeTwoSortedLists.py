# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next

            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next


a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(4)

d = ListNode(1)
d.next = ListNode(3)
d.next.next = ListNode(4)
sol = Solution()
q = sol.mergeTwoLists(a, d)

while q:
    print(q.val)
    q = q.next
