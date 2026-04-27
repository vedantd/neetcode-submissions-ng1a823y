# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        left = 0
        right = n

        if guess(left) == 0:
            return left
        if guess(right) == 0:
            return right
        

        while left < right:
            mid = (left + right) // 2

            if guess(mid) == 1:
                left = mid 
            elif guess(mid) == -1:
                right = mid 
            else:
                return mid


# left = 0
# rght = 0
# mid =  0
        