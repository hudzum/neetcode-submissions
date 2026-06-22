# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #Two Pointers
        #One Fast One Slwo
        if head is None:
            return False

        fastp = head.next
        slowp = head
        while fastp and fastp.next: #If fast == None No pointer
            #If there is a cycle fastp will eventually == slowp
            
            if fastp == slowp:
                return True
            fastp = fastp.next
            if fastp == slowp:
                return True
            fastp = fastp.next

            slowp = slowp.next
        
        return False
            