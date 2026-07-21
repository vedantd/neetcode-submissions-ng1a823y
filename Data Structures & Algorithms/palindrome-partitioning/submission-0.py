class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []
        N = len(s)

        # [a,aa]

        # add a to  []

        # is the soln [] a palindrom then add a copy

        # explore

        # add next a
        
        # making sol [aa]

        # is the soln [] a palindrom then add a copy
        def isPalindrom(s):
            start = 0
            end = len(s) -1

            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True


        def backtrack(idx, soln):

            # check if index out of bounds then check if still palindrom then add and return
            if idx == N:
                res.append(soln.copy())
                return
            
            #
            choices = []

            for i in range(idx , N):
                choices.append(s[idx:i+1])
            
            for choice in choices:
                if isPalindrom(choice):
                    soln.append(choice)
                    next_idx = idx + len(choice)
                    backtrack(next_idx, soln)
                    soln.pop()     
        backtrack(0,[])
        return res



            
                
                





        