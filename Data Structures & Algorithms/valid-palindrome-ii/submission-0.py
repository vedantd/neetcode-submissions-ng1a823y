class Solution:
    def validPalindrome(self, s: str) -> bool:

        def palindrome(arr)-> bool:
            start = 0
            end = len(arr) -1
            while start < end:
                if arr[start].lower() != arr[end].lower():
                    return False
                start +=1
                end -=1
            return True


        start = 0
        end = len(s) -1


        while start < end:
            if s[start].lower() != s[end].lower():
                # check both possibliites
                return palindrome(s[start+1: end+1]) or palindrome(s[start:end])
            start +=1
            end -=1
        return True
                    
            

                








       