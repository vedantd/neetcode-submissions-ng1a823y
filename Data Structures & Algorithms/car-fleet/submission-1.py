class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position,speed))
        cars.sort(reverse=True)  
        fleet = 0
        stack = [0]
        for i, (pos, spd) in enumerate(cars):
            
            time = (target-pos)/spd
            print(time)
            if stack and time > stack[-1]:
                stack.append(time) 


            




        return len(stack)-1
        