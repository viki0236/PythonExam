def in_range (n):
    if 0 <= n < n_matrix:
        return True
    return False

n_matrix = int(input())
n_bomb = int(input())

matrix = []

for i in range(n_matrix):
    a = []
    for j in range(n_matrix):
        a.append("0")
    matrix.append(a)
text = input()
for i in range(n_bomb):
    row = int(text[1])
    col = int(text[4])
    matrix[row][col] = "*"
    if i < n_bomb - 1:
        text = input()

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        bomb = 0

        if matrix[i][j] == "*":
            continue

        if in_range(int(j + 1)):
            if matrix[i][j + 1] == "*":
                bomb += 1

        if in_range(j - 1):
            if matrix[i][j - 1] == "*":
                bomb += 1

        if in_range(int(i + 1)):
            if matrix[i + 1][j] == "*":
                bomb += 1

        if in_range(i - 1):
            if matrix[i - 1][j] == "*":
                bomb += 1

        if in_range(int(i + 1)):
            if in_range(int(j + 1)):
                if matrix[i + 1][j + 1] == "*":
                    bomb += 1



        if in_range(i + 1):
            if in_range(j - 1):
                if matrix[i + 1][j - 1] == "*":
                    bomb += 1

        if in_range(i - 1):
            if in_range(j - 1):
                if matrix[i - 1][j - 1] == "*":
                    bomb += 1

        if in_range(i - 1):
            if in_range(j + 1):
                if matrix[i - 1][j + 1] == "*":
                    bomb += 1


        matrix[i][j] = bomb
for i in matrix:
    print(*i, sep=" ")
