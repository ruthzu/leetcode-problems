# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        current = head
        i = 1 
        while current.next:
            current = current.next
            i += 1
        k = k % i
        if k == 0:
            return head 
        current.next = head
        new_tail = head
        for j in range(i - k - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        return new_head

        