# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        fastp = head.next
        slowp = head

        while fastp and fastp.next:
            if fastp == slowp:
                return True
            fastp = fastp.next
            if fastp == slowp:
                return True
            fastp = fastp.next

            slowp = slowp.next

        return False
