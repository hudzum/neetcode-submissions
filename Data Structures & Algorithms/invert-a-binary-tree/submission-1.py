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
    #Will O(n) & O(n) for recursive stack
    #     self.swapchild(root)
    #     return root
    # def swapchild(self, root):
    #         if root:
    #             self.swapchild(root.left)

    #             self.swapchild(root.right)

    #             temp = root.right
    #             root.right = root.left
    #             root.left = temp

    #We can replicate this using a stack by 

        stack = []
        if root is None:
            return None
        
        stack.append(root)

        while stack:
            cur = stack.pop()
            temp = cur.left
            cur.left = cur.right
            cur.right = temp

            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        
        return root
    