# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """3 pointers"""
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        head = ListNode(0, head)
        k = head
        a = head.next
        b = head.next.next

        while b:
            k.next = b
            a.next, b.next = b.next, a
            a, b = b, a
            if b.next is None:
                break
            a = a.next.next
            b = b.next.next
            k = k.next.next

        return head.next
