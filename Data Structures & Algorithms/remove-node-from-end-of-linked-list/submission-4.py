# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Ambigous singly linked list or doubly linked list
        #edge cases can nth be outside of the array
        #Use cases are we going to be more traverals or insertions

        #BF Transform to array then use len to go back wards and remove element
        #then transform back into linked list
        # O(n) time and O(n) space
        # Would you like me to implement this?

        #Problems with Brute Force
        #Creating a whole array seems uneffiecient
        # From a singly linked list we have to at least O(n)
        
        dummy = ListNode(0, head) #if target is head  
        left = dummy
        right = head

        for i in range(n):
            right = right.next

        while right:
            right = right.next
            left = left.next

        left.next = left.next.next

        return dummy.next
        #dumy = -1
        #[,2] n = 2
        #l = -1
        #r = 2 (None)
        # 

