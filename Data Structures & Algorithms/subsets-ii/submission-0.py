class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(idx, soln):
            #base case
            if idx == len(nums):
                res.append(soln.copy())

                return
            
            #chooose
            
            soln.append(nums[idx])
            backtrack(idx+1, soln)
            soln.pop()

            #dont choose skip duplicates
            while idx+1 < len(nums) and nums[idx] == nums[idx +1]:
                idx = idx + 1


            backtrack(idx+1, soln)
                
        backtrack(0, [])
        return res

        