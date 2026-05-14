class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = []
        i = 0
        while i < len(temperatures):
            

            while stack and temperatures[i] > stack[-1][0]:
                
                pop = stack.pop()
                res[pop[1]]= i - pop[1]

            
            stack.append([temperatures[i],i])
            i+= 1



        return res




        