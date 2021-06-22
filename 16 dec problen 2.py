from collections import deque

text = list(input())

n = int(input())

matrix = []
row = 0
col = 0

for i in range(n):
    matrix.append(input())

final_matrix = []
for i in matrix:
    final_matrix.append([el for el in i])


for i in range(len(final_matrix)):
    for j in range(len(final_matrix[i])):
        if matrix[i][j] == "P":
            row = i
            col = j

m = int(input())

for i in range(m):
    comand = input()
    if comand == "right":
        col += 1
        if col <= len(final_matrix):
            if final_matrix[row][col] == "-":
                final_matrix[row][col] = "P"
                final_matrix[row][col - 1] = "-"
            else:
                text.append(final_matrix[row][col])
                final_matrix[row][col] = "P"
                final_matrix[row][col - 1] = "-"
        else:
            text.pop()

    elif comand == "left":
        col -= 1
        if col >= 0:
            if final_matrix[row][col] == "-":
                final_matrix[row][col] = "P"
                final_matrix[row][col + 1] = "-"
            else:
                text.append(final_matrix[row][col])
                final_matrix[row][col] = "P"
                final_matrix[row][col + 1] = "-"
        else:
            text.pop()

    elif comand == "up":
        row -= 1
        if row >= 0:
            if final_matrix[row][col] == "-":
                final_matrix[row][col] = "P"
                final_matrix[row + 1][col] = "-"
            else:
                text.append(final_matrix[row][col])
                final_matrix[row][col] = "P"
                final_matrix[row + 1][col] = "-"
        else:
            text.pop()
    elif comand == "down":
        row += 1
        if row <= len(final_matrix):
            if final_matrix[row][col] == "-":
                final_matrix[row][col] = "P"
                final_matrix[row - 1][col] = "-"
            else:
                text.append(final_matrix[row][col])
                final_matrix[row][col] = "P"
                final_matrix[row - 1][col] = "-"
        else:
            text.pop()

print(''.join(text))
for i in range(len(final_matrix)):
    for j in range(len(final_matrix[i])):
        print("".join(final_matrix[i][j]), end="")
    print()