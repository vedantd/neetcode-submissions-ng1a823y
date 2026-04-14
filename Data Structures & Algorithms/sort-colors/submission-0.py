class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # [1,0,1,2,1,0,1,2,1,0,1,2]


        # []



        zeroPointer = 0
        twoPointer = len(nums) - 1
        i = 0

        while i <= twoPointer:
            if nums[i] == 0:
                nums[zeroPointer],nums[i] = nums[i], nums[zeroPointer]
                zeroPointer += 1
                
            if nums[i] == 2:
                nums[twoPointer],nums[i] = nums[i], nums[twoPointer]
                twoPointer -=1
                i-= 1
            i+=1
        
        return nums


















        

        








        