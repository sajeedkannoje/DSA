class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
            rowSet = [set() for _ in range(9)]
            colSet = [set() for _ in range(9)]
            subgridSet = [ [set() for _ in range(3)] for _ in range(3)]

            for r in range(9):
                for c in range(9):
                    num = board[r][c]

                    if num == ".":
                        continue

                    if num in rowSet[r]:
                        return False

                    if num in colSet[c]:
                        return False

                    # subgrid check 
                    if num in subgridSet[r // 3][ c // 3]:
                        return False

                    rowSet[r].add(num)
                    colSet[c].add(num)
                    subgridSet[r // 3][ c // 3].add(num)

            
            return True