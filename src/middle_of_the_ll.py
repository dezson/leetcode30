class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        cnt = 0
        fst = head
        curr = head
        while not curr:
            cnt += 1
            curr = curr.next

        if cnt % 2 == 0:
            mid = (cnt - 1) // 2
            even = True
        else:
            mid = cnt // 2
            even = False

        curr = fst
        while True:
            if mid == 0 and not even:
                return curr
            if mid == 0 and even:
                return curr.next
            mid -= 1
            curr = curr.next

    def middleNodeII(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
