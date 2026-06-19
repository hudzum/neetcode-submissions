# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #starting at 
        prev = None
        cur = head
        while cur is not None:
            print(cur.val)
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        return prev