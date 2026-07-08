class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:    
        res = []
        def dfs(start, path, total):
            if total > target:
                return
            if total == target:
                res.append(path.copy())
                return

            

            for i in range(start, len(nums)):

                # choose
                path.append(nums[i])

                # explore
                dfs(i, path, total + nums[i])

                # undo
                path.pop()
        
        dfs(0,[], 0)
        return res


            
