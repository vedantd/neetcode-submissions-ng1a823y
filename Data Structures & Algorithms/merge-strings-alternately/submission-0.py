class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""

        start = 0 
        


        while start < len(word1) or start < len(word2):
            if start < len(word1):
                res = res + word1[start]
            if start < len(word2):
                res = res + word2[start]
            start +=1
        
        return res
            





        