class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char == "]":
                # do few things
                word = "" 
                while stack[-1] != "["     :                                   
                    pop = stack.pop()
                    word =  str(pop) + word
                number = ""
                stack.pop()
                while stack and stack[-1].isdigit():
                    number = stack.pop() +number   
                print(number)
                newword = ""
                for i in range(int(number)):
                    newword = newword + word
                stack.append(newword)
            else:    
                stack.append(char)
        return "".join(stack)


        