class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        columns = len(grid[-1])
        path = set()
        max_area = 0

        def bfs(r,c):
            q = collections.deque()

            path.add((r,c))
            q.append((r,c))
            area = 1
            while q:
                r, c = q.popleft()
                directions = [(1,0),(-1,0),(0,1),(0,-1) ]
                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc
                    if  0 <= new_r < rows and 0 <= new_c < columns and (new_r,new_c) not in path and grid[new_r][new_c]== 1:
                        path.add((new_r,new_c))
                        q.append((new_r,new_c))
                        area += 1
            return area
                    


            


        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 0 or (r,c) in path:
                    continue
                max_area = max(bfs(r,c), max_area)
                
        return max_area

        




        