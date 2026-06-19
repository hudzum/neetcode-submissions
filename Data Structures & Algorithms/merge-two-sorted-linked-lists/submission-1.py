# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #Deal with two values at a time
        #find lower first value set as head of heads
        #head list1 & list2
        #lowervalue is set to next (makesure to deal if one list is empty)
        if not list1:
            return list2
        if not list2:
            return list1
        head = list1
        cur = list1.next
        cur2 = list2
       
        if list2.val < list1.val:
            head = list2
            cur = list2.next
            cur2 = list1
        
        #print(head.next.val, cur.val)
        heady = head
        while cur2 is not None and cur is not None:
            #Compare head.next and cur
               
            if cur2.val < cur.val:
                #Continue as usual
                nxt = cur2.next
                head.next = cur2
                head = head.next
                cur2 = nxt

            else:
                #Append head with cur and swap curs
                nxt = cur.next
                head.next = cur
                head = head.next
                cur = nxt       
        #handle leftovers     
        if cur2 is not None:
            head.next = cur2
        if cur is not None:
            head.next = cur
        #print(heady)
        return heady







