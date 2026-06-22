# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        fastp, slowp = head, head

        while fastp and fastp.next:
            fastp = fastp.next.next
            slowp = slowp.next

            if slowp == fastp:
                return True

        return False
