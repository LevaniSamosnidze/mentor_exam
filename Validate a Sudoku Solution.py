# 6. Validate a Sudoku Solution
# Task Explanation:
# Write a function that validates whether a given Sudoku board is solved correctly. The board is represented as a 2D array of size 9x9. A valid solution must meet these conditions:
# Each row contains numbers 1–9 without repetition.
# Each column contains numbers 1–9 without repetition.
# Each 3x3 subgrid contains numbers 1–9 without repetition.
# Test Cases:
# 1. Valid
# Input:
# [
#     [5, 3, 4, 6, 7, 8, 9, 1, 2],
#     [6, 7, 2, 1, 9, 5, 3, 4, 8],
#     [1, 9, 8, 3, 4, 2, 5, 6, 7],
#     [8, 5, 9, 7, 6, 1, 4, 2, 3],
#     [4, 2, 6, 8, 5, 3, 7, 9, 1],
#     [7, 1, 3, 9, 2, 4, 8, 5, 6],
#     [9, 6, 1, 5, 3, 7, 2, 8, 4],
#     [2, 8, 7, 4, 1, 9, 6, 3, 5],
#     [3, 4, 5, 2, 8, 6, 1, 7, 9]
# ]

# Expected Output: True
# 2. Invalid Board with Duplicate in a Row
# Input:
# [
#     [5, 3, 4, 6, 7, 8, 9, 1, 2],
#     [6, 7, 2, 1, 9, 5, 3, 4, 8],
#     [1, 9, 8, 3, 4, 2, 5, 6, 7],
#     [8, 5, 9, 7, 6, 1, 4, 2, 3],
#     [4, 2, 6, 8, 5, 3, 7, 9, 1],
#     [7, 1, 3, 9, 2, 4, 8, 5, 6],
#     [9, 6, 1, 5, 3, 7, 2, 8, 4],
#     [2, 8, 7, 4, 1, 9, 6, 3, 5],
#     [3, 4, 5, 2, 8, 6, 1, 7, 7]  # Invalid: Two 7s in the last row
# ]

# Expected Output: False
# 3. Invalid Board with Duplicate in a Column
# Input:
# [
#     [5, 3, 4, 6, 7, 8, 9, 1, 2],
#     [6, 7, 2, 1, 9, 5, 3, 4, 8],
#     [1, 9, 8, 3, 4, 2, 5, 6, 7],
#     [8, 5, 9, 7, 6, 1, 4, 2, 3],
#     [4, 2, 6, 8, 5, 3, 7, 9, 1],
#     [7, 1, 3, 9, 2, 4, 8, 5, 6],
#     [9, 6, 1, 5, 3, 7, 2, 8, 4],
#     [2, 8, 7, 4, 1, 9, 6, 3, 5],
#     [3, 4, 5, 2, 8, 6, 9, 7, 9]  # Invalid: Two 9s in the last column
# ]

# Expected Output: False
# 4. Invalid Board with Duplicate in a 3x3 Subgrid
# Input:
# [
#     [5, 3, 4, 6, 7, 8, 9, 1, 2],
#     [6, 7, 2, 1, 9, 5, 3, 4, 8],
#     [1, 9, 8, 3, 4, 2, 5, 6, 7],
#     [8, 5, 9, 7, 6, 1, 4, 2, 3],
#     [4, 2, 6, 8, 5, 3, 7, 9, 1],
#     [7, 1, 3, 9, 2, 4, 8, 5, 6],
#     [9, 6, 1, 5, 3, 7, 2, 8, 4],
#     [2, 8, 7, 4, 1, 9, 6, 3, 5],
#     [3, 4, 5, 2, 8, 6, 1, 1, 9]  # Invalid: Two 1s in the bottom-right subgrid
# ]

# Expected Output: False
# 5. Partially Filled Board
# Input:
# [
#     [5, 3, 0, 0, 7, 0, 0, 0, 0],
#     [6, 0, 0, 1, 9, 5, 0, 0, 0],
#     [0, 9, 8, 0, 0, 0, 0, 6, 0],
#     [8, 0, 0, 0, 6, 0, 0, 0, 3],
#     [4, 0, 0, 8, 0, 3, 0, 0, 1],
#     [7, 0, 0, 0, 2, 0, 0, 0, 6],
#     [0, 6, 0, 0, 0, 0, 2, 8, 0],
#     [0, 0, 0, 4, 1, 9, 0, 0, 5],
#     [0, 0, 0, 0, 8, 0, 0, 7, 9]
# ]



def is_valid_sudoku(board):
    rows = []
    cols = []
    subgrids = []
    
    for i in range(9):
        rows.append(set())
        cols.append(set())
        subgrids.append(set())
        
    for i in range(9):
        for col in range(9):
            l = board[i][col]
            if l != 0:
                if l in rows[i]:
                    return False
                rows[i].add(l)
                
                if l in cols[col]:
                    return False
                cols[col].add(l)
                
                index = (i // 3) * 3 + col // 3
                if l in subgrids[index]:
                    return False
                subgrids[index].add(l)
                
            if l == 0:
                continue
            
            if (i + col) % 2 == 0:
                if l % 2 == 0:
                    if l % 3 == 0:
                        return False
                else:
                    if l % 5 == 0:
                        return False
            else:
                if i % 3 == 0:
                    if col % 2 == 0:
                        if l == 9:
                            return False
                        


    return True


valid_board = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

invalid_board = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 7] 
]

print(is_valid_sudoku(valid_board))  
print(is_valid_sudoku(invalid_board))  
print('თეზელ მთელი დღეა ამას ვაკეთებ ;დდდ ვიცი არ მუშაობს მარა რავი მიახლოვებულია მაინც')