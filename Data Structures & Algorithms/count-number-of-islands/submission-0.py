class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        columns = len(grid[-1])
        path = set()
        island = 0

        def bfs(r,c):
            q = collections.deque()

            path.add((r,c))
            q.append((r,c))
            while q:
                r, c = q.popleft()
                directions = [(1,0),(-1,0),(0,1),(0,-1) ]
                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc
                    if  0 <= new_r < rows and 0 <= new_c < columns and (new_r,new_c) not in path and grid[new_r][new_c]== "1":
                        path.add((new_r,new_c))
                        q.append((new_r,new_c))
                    


            


        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "0" or (r,c) in path:
                    continue
                bfs(r,c)
                island += 1
        return island

        



