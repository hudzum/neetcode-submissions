# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    # H
    #UAAAEEE
    #Use Cases 
    #Ambigious elements - Will Tree always be completed
    #Edge Cases    
    #DFS
    #Which type of order should i be using
    #Problem in order will swap the root's children therefore root.right will be root.left repeating
    #must go postfix
    #If child go up

        self.swapchild(root)
        return root
    def swapchild(self, root):
            if root:
                self.swapchild(root.left)

                self.swapchild(root.right)

                temp = root.right
                root.right = root.left
                root.left = temp