class Solution:
    def maxArea(self, heights: List[int]) -> int:

        start = 0
        end = len(heights) - 1
        max_area = float("-inf")

        while start < end:
            area = min(heights[start], heights[end]) * (end - start)
            if area > max_area:
                max_area = area
            # comapre and decide which ptr to move
            if heights[start] > heights[end]:
                end -= 1
            else:
                start += 1
        
        return max_area
            




        