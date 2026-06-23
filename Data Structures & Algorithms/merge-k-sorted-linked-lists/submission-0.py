# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #UAE
        #will are there gonna be more values within each linked list or the array that hold them
        #Edge Cases can the inner linked list be empty
        #Ambigious are values going ot be purely integers

        #append each linked list to a massive linked list and then convert to array
        #then sort O(nlogn) Space of O(n)
        #Would you like me to implement this

        #Problems with BF
        #linked list usually can update within themselves so space of O(n) seems ineffiecent
        
        #We can merge in place time O(m+n) of two linked list and O(1) space
        #and for each linkedlist in teh array O(m+n+k+j...)

        if not lists:
            return None
        def merge_ll(head1, head2):
            dummy = node = ListNode()

            while head1 and head2:
                if head1.val < head2.val:
                    node.next =head1
                    head1 = head1.next 
                else:
                    node.next = head2
                    head2 = head2.next

                node = node.next
            node.next = head1 or head2
            return dummy.next
        
        
        res = lists[0]
        for i in range(1, len(lists)):
            res = merge_ll(res, lists[i])
        
        return res


