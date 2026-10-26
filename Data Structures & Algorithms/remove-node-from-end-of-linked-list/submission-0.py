class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        prev = dummy
        for _ in range(length - n):
            prev = prev.next

        prev.next = prev.next.next
        return dummy.next