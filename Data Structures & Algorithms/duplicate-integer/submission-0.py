class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hm = {}
        # N  = len(nums) 
        # for i in range(0,N):
        #     print(nums[i])
        #     print(hm)
        #     if nums[i] in hm:
                
        #         return True
        #     else:
        #         hm[nums[i]] = 0 
        
        # return False
        uniqueset = set()
        N=len(nums)
        for i in range(0,N):
            if nums[i] in uniqueset:
                return True
            else:
                uniqueset.add(nums[i])

        return False

        
        