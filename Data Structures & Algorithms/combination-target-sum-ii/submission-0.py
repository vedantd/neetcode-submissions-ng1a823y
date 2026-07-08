class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        uni = sorted(candidates)
      

        res = []

        def dfs(start, path, tot):
            
            
            if tot == target:
                res.append(path.copy())
                return
            if start == len(uni):
                return
            
            elif tot > target:
                return
            
            else:
                for i in range(start, len(uni)):
                    if i > start and uni[i] == uni[i-1]:
                        continue
                     
                    path.append(uni[i]) # choose

                    dfs(i+1,path,tot + uni[i]) #explore

                    path.pop()
        dfs(0,[],0)
        return res

        