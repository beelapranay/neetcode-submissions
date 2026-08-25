class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                if(rows[i] in rows
                or cols[j] in cols
                or squares[(i, j)] in squares[(i//3, j//3)]):
                    return False

                rows.add(i)
                cols.add(j)
                squares.add(i//3, j//3)
        return True        