class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            sets = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in sets:
                    return False 
                sets.add(board[i][j])
        
        for i in range(9):
            sets = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in sets:
                    return False
                sets.add(board[j][i])
                
            
        for square in range(9):
            sets = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in sets:
                        return False
                    sets.add(board[row][col])
        
        return True






