"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #Ambiguous are nodes values unique???
        #Either DFS or BFS to traverse through the graph using a set or hashmap to stop cycling
        if not node:
            return None
        oldToNew = {}

        copy = Node(node.val)
        oldToNew[node] = copy

        q = deque()
        q.append(node)

        while q:
            cur = q.popleft()
            for nb in cur.neighbors:
                if nb not in oldToNew:
                    nbc = Node(nb.val)
                    oldToNew[nb] = nbc
                    q.append(nb)
                oldToNew[cur].neighbors.append(oldToNew[nb])

        


        return copy

