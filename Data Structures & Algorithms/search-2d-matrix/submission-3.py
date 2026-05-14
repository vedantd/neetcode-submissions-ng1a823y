class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix)

        row = 0
        column = 0

        while start < end:
            mid = (start+end)//2
            if target < matrix[mid][-1]:
                end = mid 
            elif target > matrix[mid][-1]:
                start = mid+1
            else:
                return True
        if start == len(matrix):
            return False
        left = 0
        right = len(matrix[0])
        while left < right:
            mid = (left+right)//2
            if target < matrix[start][mid]:
                right = mid
            elif target > matrix[start][mid]:
                left = mid + 1
            else:
                return True
        return False



                 



        