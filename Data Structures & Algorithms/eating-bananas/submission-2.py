
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        left = 1
        right = max(piles)

        

        while left < right:
            k = (left + right)//2
            time = 0
            for pile in piles:
                time = time + math.ceil(float(pile)/k)
            if time <= h:
                right = k 
            else:
                left = k + 1


        return left 



                           

            








# [4,10,23,25]
# [1,2,3,4,5,...25]


# h = 9


