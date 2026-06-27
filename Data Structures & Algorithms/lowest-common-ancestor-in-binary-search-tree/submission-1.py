# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #Edge Cases Will both nodes always exists?, Will p less than q
        #Use Cases should i expect nodes to be close to the top or bottom
        #Ambigiuous will q every equal q

        #Brute Force : At every node do dfs till we find both q and p. if not we move too next node
        #O(n^2) because we are runnign DFS for every node which is O(n)
        #O(h+h) stack depth and stuff
        #We really dont need to be checking every node just determinign the pattern node once weve found
        #our targets

        #Given the BST and we have two nodes
        #can we compare p and q such that we know its a parent

        # if root.val <= p.val and root.val >=q.val:
        #     return root
        # #Incase q> p
        # if root.val >= p.val and root.val <=q.val:
        #     return root
        
        # #Now root is not between q or p
        # if p.val > root.val:
        #     return self.lowestCommonAncestor(root.right, p ,q)
        # else:
        #     return self.lowestCommonAncestor(root.left, p , q)

        #ISSUE Recursion causes space to be O(h) heihgt

        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur

        #What should happen if cur is None
