class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        n = len(nums)

        def binarySearch(left: int, right: int) -> int:
            
            while left <= right:
                mid = (left +right)//2
                if nums[mid] < target:
                    left = mid +1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    return mid
            return -1

        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        

            

        pivot = l

        if nums[pivot] <= target <= nums[n - 1]:
            return binarySearch(pivot, n - 1)
        else:
            return binarySearch(0, pivot - 1)


        