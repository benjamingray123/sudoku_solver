example_board = [
        [3, 9, 0,   0, 5, 0,   0, 0, 0],
        [0, 0, 0,   2, 0, 0,   0, 0, 5],
        [0, 0, 0,   7, 1, 9,   0, 8, 0],

        [0, 5, 0,   0, 6, 8,   0, 0, 0],
        [2, 0, 6,   0, 0, 3,   0, 0, 0],
        [0, 0, 0,   0, 0, 0,   0, 0, 4],

        [5, 0, 0,   0, 0, 0,   0, 0, 0],
        [6, 7, 0,   1, 0, 5,   0, 4, 0],
        [1, 0, 9,   0, 0, 0,   2, 0, 0]
    ]

def find_next_empty(puzzle):
    ''' locates next empty (0) cell, returns index (r,c). returns (None,None) if board complete. '''
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == 0:
                return (r, c)        
    return (None, None)

def is_valid(puzzle, guess, row, col):
    ''' checks row, col, square for validity. returns True or False '''
    if guess in puzzle[row]: #rows
        return False
    if guess in [puzzle[r][col] for r in range(9)]: #cols
        return False

    row_start = (row // 3)*3 # // intdiv *3 = index of topleft element in square 
    col_start = (col // 3)*3 # 
    for r in range(row_start, row_start+3): #squares
        for c in range(col_start, col_start+3):
            if puzzle[r][c] == guess:
                return False
    return True 
         
def solve_sudoku(puzzle):
    ''' calls find_next_empty().
        if is_valid(): submits guess in cell.
        if not is_valid(): assigns cell = 0, try again with different guess (backtracking)
        function calls itself (recursion) until true or all guesses spent (unsolvable puzzle) '''
    row, col = find_next_empty(puzzle)
    if row is None:
        return True
    for guess in range(1,10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):
                return True
        #invalid guess resets cell 
        puzzle[row][col] = 0

    return False #guesses exhausted - puzzle unsolvable 

if __name__ == '__main__':
    print(solve_sudoku(example_board))
    print(example_board)
    

        
        
    
    
