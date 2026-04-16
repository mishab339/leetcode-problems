class solution:
    def pacificAtlantic(self,height:list[list[int]])->list[list[int]]:
        ROWS,COLS = len(height),len(height[0])
        pac,atl = set(),set()

        def dfs(r,c,visit,prevHeight):
            if((r,c) in visit or r<0 or c<0 or r==ROWS or c==COLS or height[r][c] < prevHeight):
                return
            visit.add((r,c))

            dfs(r + 1, c, visit, height[r][c])
            dfs(r - 1, c, visit, height[r][c])
            dfs(r, c + 1, visit, height[r][c])
            dfs(r, c - 1, visit, height[r][c])
        
        for c in range(COLS):
            dfs(0,c,pac,height[0][c])
            dfs(ROWS - 1, c, atl, height[0][c])
        
        for r in range(ROWS):
            dfs(r,0,pac,height[r][0])
            dfs(r, COLS - 1, atl, height[r][0])
        
        result = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    result.append((r,c))

        return result;