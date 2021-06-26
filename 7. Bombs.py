def is_in_range(row, n):
    if 0 <= row < n:
        return True
    return False

n = int(input())

matrix = []
matrix_chec = []
for i in range(n):
    matrix.append([int(el) for el in input().split()])



bomb  = input().split()


alive_cells = 0

for i in bomb:
    row, col = [int(el) for el in i.split(",")]
    if is_in_range(row, n) and is_in_range(col, n):
        b = int(matrix[row][col])
        matrix[row][col] = 0
        up_row = row - 1
        if is_in_range(up_row, n):
            if not [up_row, col] in matrix_chec:
                matrix[up_row][col] = matrix[up_row][col] - b
                if matrix[up_row][col] <= 0:
                    matrix_chec.append([up_row, col])

        down_row = row + 1
        if is_in_range(down_row, n):
            if not [down_row, col] in matrix_chec:
                matrix[down_row][col] = matrix[down_row][col] - b
                if matrix[down_row][col] <= 0:
                    matrix_chec.append([down_row, col])

        left_col = col - 1
        if is_in_range(left_col, n):
            if not [row, left_col] in matrix_chec:
                matrix[row][left_col] = matrix[row][left_col] - b
                if matrix[row][left_col] <= 0:
                    matrix_chec.append([row, left_col])

        right_col = col + 1
        if is_in_range(right_col, n):
            if not [row, right_col] in matrix_chec:
                matrix[row][right_col] = matrix[row][right_col] - b
                if matrix[row][right_col] <= 0:
                    matrix_chec.append([row, right_col])

        up, left = row - 1, col - 1
        if is_in_range(up, n) and is_in_range(left, n):
            if not [up, left] in matrix_chec:
                matrix[up][left] = matrix[up][left] - b
                if matrix[up][left] <= 0:
                    matrix_chec.append([up, left])

        up, right = row - 1, col + 1
        if is_in_range(up, n) and is_in_range(right, n):
            if not [up, right] in matrix_chec:
                matrix[up][right] = matrix[up][right] - b
                if matrix[up][right] <= 0:
                    matrix_chec.append([up, right])


        down, left = row + 1, col - 1
        if is_in_range(down, n ) and is_in_range(left, n):
            if not [down, left] in matrix_chec:
                matrix[down][left] = matrix[down][left] - b
                if matrix[down][left] <= 0:
                    matrix_chec.append([down, left])

        down, right = row + 1, col + 1
        if is_in_range(down, n) and is_in_range(right, n):
            if not [down, right] in matrix_chec:
                matrix[down][right] = matrix[down][right] - b
                if matrix[down][right] <= 0:
                    matrix_chec.append([down, right])



for i in bomb:
    row, col = [int(el) for el in i.split(",")]
    if is_in_range(row, n) and is_in_range(col, n):
        b = int(matrix[row][col])
        matrix[row][col] = 0
s = 0
for r in range(n):
    for c in range(n):
        if matrix[r][c] > 0:
            alive_cells += 1
            s += matrix[r][c]

print(f"Alive cells: {alive_cells}")
print(f"Sum: {s}")

for i in matrix:
    print(*i, sep=" ")