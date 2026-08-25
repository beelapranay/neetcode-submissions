class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set);
        cols = collections.defaultdict(set);
        squares = collections.defaultdict(set);

        for i in range(9):
            for j in range(9):
                if(board[i][j] == "."):
                    continue
                if(board[i][j] not in rows[i]
                or board[i][j] not in cols[j]
                or board[i][j] not in squares[(i//3, j//3)]):
                    return False
                rows.add(board[i][j])
                cols.add(board[i][j])
                squares.add()       
        