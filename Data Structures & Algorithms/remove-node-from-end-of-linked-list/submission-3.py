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
        dummy = ListNode(0,head)
        first, second = dummy, head
    
        for i in range(n):
            second = second.next

     
        while second:
            first = first.next
            second = second.next
        
        first.next = first.next.next

        return dummy.next
        #1, 2, 3, 4
        #second = 3
        #first = 1
        #2 -> None

        #[1,2, None]
        #n = 2
        #second = None
        #first =1
        #First should be incremented by one

