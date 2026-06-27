# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #Edge Case - Do subtrees reach all the way to leaves or can stop midway, they do
        #useCases - 
        #Ambigious - What can we expect regarding tree balance
        #Is none a subroot of every tree??
        #I think DFS and as soon as subroot and tree == then start scannign
        #when they dont equal before going back to subroot return false
        #DFS because it automatically scans subtree by subtree
        if not root and subRoot:
            return False
        if self.sameTree(root,subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        return False

    def sameTree(self, root, root2):
        #if root 1 and root2 == that mean start of potential subroot
        #if they don' t keep searching?
        if not root and not root2: #Base Case Both are none (children of leafs)
            return True
        
        #If one is none while the other isn't or if values don't match
        if not root or not root2 or root.val != root2.val:
            return False
        else:
            return self.sameTree(root.left, root2.left) and self.sameTree(root.right, root2.right)

