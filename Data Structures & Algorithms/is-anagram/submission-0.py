class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm = {}
        if len(s) != len(t):
            return False

        for i in s:
            if i not in hm:
                hm[i] = 1

            else:
                hm[i]+=1

         
        print(hm)

        for j in t:
            if j not in hm:
                return False
            

            else:
                if hm[j] == 0:
                    return False
                
                hm[j] -= 1

        
        return True
            

               
            

