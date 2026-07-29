class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:



        ROWS = len(heights)
        COLUMNS  = len(heights[-1])
        path_atl = set()
        path_pcf = set()

        def dfs(r ,c, path , prev):
            if r < 0 or r == ROWS or c < 0 or c == COLUMNS or heights[r][c] < prev or (r,c) in path:
                return
            
            path.add((r,c))

            dfs(r+1 ,c, path , heights[r][c])
            dfs(r -1,c, path , heights[r][c])
            dfs(r ,c+1, path , heights[r][c])
            dfs(r ,c-1, path , heights[r][c])
                
        
        for c in range(COLUMNS):
            dfs(0, c ,path_pcf ,heights[0][c])
            dfs(ROWS-1 , c ,path_atl, heights[ROWS-1][c] )
        
        for r in range(ROWS):
            dfs(r, 0 ,path_pcf ,heights[r][0])
            dfs(r , COLUMNS-1 ,path_atl, heights[r][ COLUMNS-1] )
        return list(path_atl & path_pcf)
        







        