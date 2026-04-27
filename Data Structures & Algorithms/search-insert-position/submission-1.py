class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) 
        
        while left < right:
            print(left, right)
            mid = (left + right)//2
            if nums[mid] < target:
                left = mid + 1
            
            else:
                right = mid
                
        
        return left

        #  nums = [-1,0,2,4,6,8]
        #         [ 0,1,2 3 4 5]   
        #         LEFT = 3 
        #         RIGTH = 5
        #         MID = 3+5//2 = 4



        