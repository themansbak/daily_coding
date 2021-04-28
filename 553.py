"""
You are given an N by M 2D matrix of lowercase letters. Determine the minimum number of columns that can be removed to ensure that each row is ordered from top to bottom lexicographically. That is, the letter at each column is lexicographically later as you go down each row. It does not matter whether each row itself is ordered lexicographically.

e.g.

cba
daf
ghi
=> remove 2nd column

Algorithm:
- Go through each column
    - compare whether or not the previous character is lexographically
        smaller than the current char
    - if it is then we update our invalid counter by 1
        - move onto the next column
- return the invalid counter
"""

matrices = [
    [
        ['c','b','a'],
        ['d','a','f'],
        ['g','h','i']
    ],
    [
        ['c','a'],
        ['d','f'],
        ['g','i']
    ],
    [
        ['a','b','c']
    ],
    [
        ['z','y','x'],
        ['w','v','u'],
        ['t','a','r']
    ]
]

def count_invalid_columns(matrix):
    n = len(matrix)
    m = len(matrix[0])
    invalid_count = 0

    for y in range(m):
        prev = 0 # we can use a temp character to compare against
        for x in range(n):
            if ord(matrix[x][y]) < prev:
                invalid_count += 1
                break
            prev = ord(matrix[x][y])
    return invalid_count

def check_matrices(matrices):
    for matrix in matrices:
        print(count_invalid_columns(matrix))


check_matrices(matrices)
