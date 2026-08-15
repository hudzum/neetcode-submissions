class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #We can find all the cells that can flow into atl or pac
        #find which cells are in both. return 

        #Starting from borders we can run dfs on each 
        #if neighbor is heigher or equal + in bounds and not in visited
        #Add visited run dfs
        #to check if heigher use a prevheight param in dfs
        atl, pac = set(), set()
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        rows , cols = len(heights),  len(heights[0])

        def dfs(r, c, visitSet, prevHeight):
            if r < 0 or c < 0 or r >= rows or c >= cols or heights[r][c] < prevHeight or (r,c) in visitSet:
                return 
            visitSet.add((r,c))
            for dr , dc in directions:
                nr, nc = r+dr, c + dc
                dfs(nr,nc, visitSet, heights[r][c])



        for c in range(cols):
            #run top and bot rows
            dfs(0, c, pac, heights[0][c])
            dfs(rows-1, c, atl, heights[rows-1][c])

        for r in range(rows):

            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols-1, atl, heights[r][cols-1])

        res = []
        for r, c in atl:
            if (r,c) in pac:
                res.append((r,c))

        return res




        
                

