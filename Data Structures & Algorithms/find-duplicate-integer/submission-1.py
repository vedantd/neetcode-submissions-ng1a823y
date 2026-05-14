class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        N = len(nums)

        for i in range(N):
            idx = abs(nums[i])
            if nums[idx] < 0:
                return idx

            nums[idx] = -1*nums[idx]
        


























        # N = len(nums)

        # [1,2,3,4,4]
        # [-1,-2]

        # for i in range(N):
            
        #     idx = abs(nums[i])
        #     if nums[idx] < 0:
        #         return idx
        #     nums[idx] = -1 * nums[idx]