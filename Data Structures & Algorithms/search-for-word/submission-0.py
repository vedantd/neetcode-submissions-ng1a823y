class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLUMNS = len(board[-1])
        path = set()



        def backtrack(row, column, idx):

            if idx == len(word):
                return True
            if row < 0 or row >= ROWS or column < 0 or column >= COLUMNS:
                return False
            
            
            

            if board[row][column] != word[idx]:
                return False
            


            if (row,column) in path:
                return False
            path.add((row,column))
            res = backtrack(row + 1, column, idx + 1 ) or backtrack(row - 1, column,  idx + 1  ) or backtrack(row, column +1,  idx + 1 ) or backtrack(row, column -1,idx + 1  )

            path.remove((row,column))
            return res
        
        for row in range(ROWS):
            for column in range(COLUMNS):
                if backtrack(row,column,0 ):
                    return True

        return False    #unselect





            # base case
            # if row or column is out of bounds
            # if idx is out of bounds of word we return
            # if char in not matching to word[idx] return
            # if char is matching but alreday in path return
            # implied that char is not in. path and matching now
            # backtrack with next idx (visit up down lleft rirght) pass path
            # if nayt of those return true its found
            # if they dont then unselect path.pop 


            #what i dont understnad is where we unselect and try some other choice is this




        

