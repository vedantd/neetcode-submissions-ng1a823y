class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        left = 0 
        right = len(people) - 1
        count = 0
        while left <= right:

            total = people[left] + people[right]

            if total < limit:
                count += 1
                left += 1
                right -=1
            elif total > limit:
                right -= 1
                count += 1
            else:
                count += 1
                left += 1
                right -= 1
        

        return count






        