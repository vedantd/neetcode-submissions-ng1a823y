class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # extract all the tresures

        ROWS = len(grid)
        COLUMNS = len(grid[-1])
        p = collections.deque()
  
                        
        for r in range(ROWS):
            for c in range(COLUMNS):
                if grid[r][c] == 0:
                    p.append([r,c])
                # if grid[r][c] == 2147483647:
                #     grid[r][c] = 0



        directions = [[1,0],[-1,0],[0,-1],[0,1]]
        while p:
            for _ in range(len(p)):
                r , c = p.popleft()
                for dr , dc in directions:
                    new_r = r + dr
                    new_c = c + dc

                    if new_r < 0 or new_r >= ROWS or new_c < 0 or new_c >= COLUMNS or grid[new_r][new_c]== 0 or  grid[new_r][new_c]== -1 or grid[new_r][new_c] != 2147483647:
                        continue
                                        
                    p.append([new_r,new_c])
                    grid[new_r][new_c] =  grid[r][c] + 1
            
        



        



