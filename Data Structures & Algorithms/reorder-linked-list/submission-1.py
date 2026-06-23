# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Divide the List in two
        sp, fp = head, head.next
        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next 
        
        #Now SP is mid point
        #Reverse Second List 

       
        second = sp.next
        prev = sp.next = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        #Merge
        second = prev
        first = head
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
            
        return None
