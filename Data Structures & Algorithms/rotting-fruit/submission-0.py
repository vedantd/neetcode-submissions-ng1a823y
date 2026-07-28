class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        p = collections.deque()
        ROWS = len(grid)
        COLUMNS = len(grid[-1])
        fresh = 0
        time = 0
        

        for r in range(ROWS):
            for c in range(COLUMNS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    p.append([r,c])
                else:
                    continue


        # we have the count of fresh oranges, we have extrtacted the rotten orange in a queue
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        while p and fresh > 0:
            for _ in range(len(p)):
                r, c = p.popleft()
                for dr , dc in directions:
                    new_r = r + dr
                    new_c = c + dc
                    if   new_r < 0 or  new_r >= ROWS or new_c  < 0 or new_c >= COLUMNS or grid[new_r][new_c] != 1:
                        continue
                    grid[new_r][new_c] = 2
                    fresh -=1
                    p.append([new_r, new_c])
            time += 1
        
        if fresh <= 0:
            return time
        else:
            return -1
                    







        
        
