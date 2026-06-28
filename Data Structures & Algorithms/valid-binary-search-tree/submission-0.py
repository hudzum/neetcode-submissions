# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #Okay
        #Ambigious can children nodes be equal
        #Edge cases whats the state of binary tree completed full or wil there be nones
        #Use Cases

        #So first off BF we can use dfs to go through each node 
        #if children exist we check if left and right exist and are correct less than or greater than
        #this would be big O(n) and space O(1) 
        #Would you like me to code this out?
        
        #using Hint using DFS along with an interval
        #check if root is between -inf and +inf
        #going to right set interval as 6, +inf
        #going to left set int as -inf, 6]
        return self.CheckInterval(float('-inf'), float('+inf'), root)

        
    def CheckInterval(self, lowerBound, upperBound, root):
        if root is None:
            return True
        
        if root.val > lowerBound and root.val < upperBound:
            return self.CheckInterval(lowerBound, root.val,root.left) and self.CheckInterval(root.val, upperBound, root.right)
        
        else:
            return False

        

