# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    count = 0
    res = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #Use Cases
        # Ambigious
        #Edge Cases\

        #BFS is to DFS through the array to find the lowest pop or save it
        #, then repeat k times
        #this would be O(n^2) time 
        #main issue we are constantly repeatedly searching that array over and over again
        #Convert to Heap O(n)
        #Pop from heap to get that lowest element

        #DFS In ordeer to keep 
        #IM STUPID IN ORDER TRAVERSAL IS LITERALLY LEAST TO GREATEST ON BST
        val = self.smallest(root)
        return self.res
    def smallest(self,root):
        if root.left:
           self.smallest(root.left)
       
        self.count += 1 
        if self.count == k:
            self.res = root.val
            return
        if root.right:
            self.smallest(root.right)
      