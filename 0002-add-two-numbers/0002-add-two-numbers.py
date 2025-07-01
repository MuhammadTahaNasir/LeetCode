class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l1  # Reuse l1 as the output list
        prev = None
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry

            if l1:
                l1.val = total % 10
                carry = total // 10
                prev = l1
                l1 = l1.next
            else:
                prev.next = ListNode(total % 10)
                prev = prev.next
                carry = total // 10

            if l2:
                l2 = l2.next

        return head
