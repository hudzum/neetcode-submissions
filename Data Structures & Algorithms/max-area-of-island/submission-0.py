class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #BFS but during queue stage of searching each island count the size
        rows, cols = len(grid), len(grid[0])
        maximumSize = 0
        visited = set()

        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        def bfs(r,c):
            size = 1
            q = deque()
            visited.add((r,c))
            q.append((r,c))

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if nr >= 0 and nc >= 0 and nr < rows and nc < cols:
                        if grid[nr][nc] == 1 and (nr,nc) not in visited:
                            visited.add((nr, nc))
                            q.append((nr, nc))
                            size +=1 

            return size





        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    size = bfs(r,c)
                    maximumSize = max(size, maximumSize)

        return maximumSize