# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #Ambigious can i expect nodes to be null
        #Use Cases
        ##Edge Cases Hey is the tree full?
        
        #How do we loop through BST so we can add level by level

        q = deque()
        res = []

        q.append(root)
        while q:
            qlen = len(q) #current level amount
            sublevel = []
            for i in range(qlen): #each element at current level
                
                cur = q.popleft()
                if cur: #what to do if cur is None
                    print(qlen, cur.val)
                    sublevel.append(cur.val)
                    q.append(cur.left)
                    q.append(cur.right)
            if sublevel: #Incase blank
                res.append(sublevel)


        return res