# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None #Making Sure No Cycles
        # 1 -> 2 -> 3
        while cur is not None:
            nxt = cur.next # 2
            cur.next = prev # 1 -> None
            prev = cur # 1
            cur = nxt # 2

        return prev