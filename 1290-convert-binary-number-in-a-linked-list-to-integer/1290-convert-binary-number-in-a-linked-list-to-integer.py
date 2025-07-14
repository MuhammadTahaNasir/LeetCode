class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = 0
        while head:
            num = (num << 1) | head.val
            head = head.next
        return num
