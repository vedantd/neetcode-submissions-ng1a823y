class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # start end pointer at a value lesser than target
        end = 0
       
        end = len(numbers)-1    
        start = 0

        while start < end:

            tot = numbers[start] + numbers[end]
            print(tot)
            if tot < target:
                start += 1
            elif tot > target:
                end-=1
            else:
                
                return[start +1, end+1]

       
                