# Definition for a binary tree node.
# class TreeNode: 
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #bfs or dfs store the longest we traversed down from root
        #UAE
        #Use Case Is our solution likely to be near the top level or bottom levels
        #Ambigious What is the completion state of our binary tree Balanced, Full, Complete
        #Edge Cases are some of our leaf nodes going to be null

        #BF For each node check its children node loop and count the highest
        #We repead too much for the longer binary trees

        #BFS vs DFS 
        #Will we need to go through each node once
        #DFS but everytime we go up or down we update a global level variable
        #if higher then the highest max compare highest
        self.curlevel = 0
        self.highestlev = 0

        self.countlevel(root)
        return self.highestlev
    def countlevel(self, root):
        if root:
            self.curlevel+=1
            self.highestlev = max(self.highestlev, self.curlevel)
            self.countlevel(root.left)
            self.countlevel(root.right)
            self.curlevel-=1

        

