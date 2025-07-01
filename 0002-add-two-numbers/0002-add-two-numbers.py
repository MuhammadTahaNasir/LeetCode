class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = l1  # Reuse l1 to save space
        prev = None
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + carry

            if l1:
                l1.val = total % 10
                carry = total // 10
                prev = l1
                l1 = l1.next
            else:
                prev.next = ListNode(total % 10)
                carry = total // 10
                prev = prev.next

            if l2:
                l2 = l2.next

        return head
