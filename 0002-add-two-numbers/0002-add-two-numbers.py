class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        p, q, curr = l1, l2, dummy
        carry = 0
        while p or q:
            x = p.val if p else 0
            y = q.val if q else 0
            s = carry + x + y
            carry = s // 10
            curr.next = ListNode(s % 10)
            curr = curr.next
            if p: p = p.next
            if q: q = q.next
        if carry:
            curr.next = ListNode(carry)
        return dummy.next
