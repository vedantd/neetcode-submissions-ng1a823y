class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        N = len(digits)
        res = []

        self.maps =  {"2": "abc","3":"def","4": "ghi","5": "jkl","6": "mno", "7": "pqrs","8": "tuv","9": "wxyz"}
        

        
        def backtrack(idx, soln):
            
            # if length of word is reached add copy of sol to res
            # if not then 
            
            if len(soln) == N:
                res.append(soln)
                return
            # if not then 
            
            curr = digits[idx]
            choices = self.maps[curr]

            for choice in choices:
                backtrack(idx+1, soln + choice )
            
        backtrack(0,"")
        return res
            #unselect
            



            




        return []