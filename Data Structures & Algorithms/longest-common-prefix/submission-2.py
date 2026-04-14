class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word = strs[0]
        N = len(first_word)
        

        for i in range(N):
            char_to_match =  first_word[i]
            print(char_to_match)

            for other_word in strs[1:]:
                if i >= len(other_word) or other_word[i] != char_to_match:
                    return first_word[:i]

        return first_word
           






            

                



        