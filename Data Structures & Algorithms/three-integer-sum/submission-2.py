class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []            
        curr = 0
        print(nums)
        while curr  < len(nums) - 2:
            if curr > 0 and nums[curr] == nums[curr - 1]:
                curr += 1
                continue
            start = curr + 1
            end = len(nums) - 1
            while start < end:
                tot = nums[start]+nums[end]+ nums[curr]
                
                if  tot > 0:
                    end -=1
                elif tot < 0:
                    start += 1            
                else:    
                    res.append([nums[curr],nums[start],nums[end]])
                    start += 1
                    end -= 1
                    while start < end and nums[start] == nums[start - 1]:
                        start += 1

                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1
            curr +=1
            
        return res






        



