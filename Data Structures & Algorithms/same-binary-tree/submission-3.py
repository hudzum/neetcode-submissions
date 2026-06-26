# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #UAEE
        #Use Cases - We will our answer be colser to the root or to the leves
        #Ambigious - Will this be a binary tree or possible have n children
        #Edge Cases - Is there a chance that trees will be unbalanced

        #BFS OR DFS no matter what we are not gonna use a I think I'll choose dfs
        #because we are targetting the first wrong change. trees can really differ 
        #at any time
        #So DFS through both at same time comparing each element, 2 stacks
        #In order to compare each node at the same time
        stack, stack2 = [p], [q]
        #Example: [4, 5] [4, Null, 5]
        #Stack 1 [5,]
        #stack 2 [Null]
      
        while stack or stack2: #If a tree has one more leaf and other doesn't will end loop before checking
            cur, cur2 = stack.pop(), stack2.pop()
            if not cur and not cur2:
                continue #Basically incase both empty
            #Basically doesn't check None
            if not cur or not cur2 or cur.val != cur2.val:
                return False

            if cur.left or cur2.left:
                stack.append(cur.left)
                stack2.append(cur2.left)


            if cur.right or cur2.right:
                stack.append(cur.right)
                stack2.append(cur2.right)
            
        return True
