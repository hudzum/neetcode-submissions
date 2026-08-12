class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        #First Find Chest
        #BFS from chest 
        q = deque()
        visited = set()

        #Find Chest
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c,0))
                    visited.add((r,c))


        while q:
            r, c, prev = q.popleft()

            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                #check bounds then visited and -1
                if nr < rows and nr >= 0 and nc < cols and nc >=0:
                    if (nr,nc) not in visited and grid[nr][nc] != -1:
                        #how to keep track of every level
                        grid[nr][nc] = prev+1
                        visited.add((nr,nc))
                        q.append((nr,nc,prev+1))

                    
        print(grid)