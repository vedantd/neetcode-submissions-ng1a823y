class Solution:
    def isPalindrome(self, s: str) -> bool:   
        start = 0
        end = len(s) - 1

        def isAlphabet(c)-> bool:
            if 96 < ord(c) < 123 or 64 < ord(c) < 91 or 48 <= ord(c) <= 57:
                return True
            return False
            
        while start < end:
            print(s[start])
            print(s[end])
            if isAlphabet(s[start]) == False: 
                while isAlphabet(s[start]) == False and start < end:
                    start += 1
                                 
            if isAlphabet(s[end]) == False:
                while  isAlphabet(s[end]) == False and start < end:
                    end -= 1    
            print(s[start], s[end])
            if s[start].lower() != s[end].lower():
                return False
            start +=1
            end -=1


        return True 