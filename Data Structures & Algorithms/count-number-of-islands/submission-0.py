class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        def bfs(r, c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr+r, dc+c
                    #check if in bounds
                    #check for visited and 1
                    if nr >= 0 and nr < rows and nc >= 0 and nc < cols:
                        if (nr,nc) not in visited and grid[nr][nc] == "1":
                            q.append((nr, nc))
                        visited.add((nr, nc))      

        for r in range(rows):
            for c in range(cols):
                if r >= 0 and r < rows and c >= 0 and c < cols:
                    if (r,c) not in visited and grid[r][c] == "1":
                        bfs(r,c)
                        res += 1

        return res

        