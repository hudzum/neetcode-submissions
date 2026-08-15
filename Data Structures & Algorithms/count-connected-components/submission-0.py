class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #Create Adj list undirected
        #
        adjMap = {i:[] for i in range(n)}
        for edg, adj in edges:
            adjMap[adj].append(edg)
            adjMap[edg].append(adj)

        #Once DFS completed an entire graph will be in visited
        visited = set()
        def dfs(node):
            if node in visited:
                return False
            visited.add(node)
            for nei in adjMap[node]:
                dfs(nei)

            return True

        res = 0
        for i in range(n):
            if dfs(i):
                res +=1 

        return res