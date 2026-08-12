class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        atl = set()
        pac = set()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        #Get  rows 0, and
        

        def dfs(r,c, visitSet, prevheight):
            if (r < 0 or c <0 or c == cols or r == rows
                    or heights[r][c] < prevheight or (r, c) in visitSet):
                        return
            visitSet.add((r,c))
            for dr, dc in directions:
                nr, nc = dr+r, dc+c

                dfs(nr,nc, visitSet,heights[r][c])
        
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows-1, c, atl, heights[rows-1][c])
        
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols-1,atl, heights[r][cols-1])
        print(atl)
        print(pac)
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res



        
                

