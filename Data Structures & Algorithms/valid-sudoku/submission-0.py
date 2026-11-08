class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0, 9):
            visitedForRow = set()
            visitedForColumn = set()
            for j in range(0, 9):
                if board[i][j] != ".":
                    if board[i][j] in visitedForRow:
                        return False
                    else:
                        visitedForRow.add(board[i][j])

                if board[j][i] != ".":
                    if board[j][i] in visitedForColumn:
                        return False
                    else:
                        visitedForColumn.add(board[j][i])

        for i in range(0, 3):
            for j in range(0, 3):
                visitedForSubBoard = set()
                for k in range(0, 3):
                    for l in range(0, 3):
                        cell = board[i * 3 + k][j * 3 + l]
                        if cell != ".":
                            if cell in visitedForSubBoard:
                                return False
                            else:
                                visitedForSubBoard.add(cell)

        return True
        