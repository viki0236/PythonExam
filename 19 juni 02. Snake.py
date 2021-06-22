def chek(ch):
    if 0 <= ch <= len(matrix) - 1:
        return True
    return False

n = int(input())
m = []


for i in range(n):
    m.append(input())

matrix = []
for i in m:
    matrix.append([el for el in i])
row = 0
col = 0

food = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "S":
            row = i
            col = j
            break
comand = input()

flag = True
while flag:
    if comand == "up":
        s = matrix[row][col]
        row -= 1
        if chek(row):
            if matrix[row][col] == "*":
                food += 1
                matrix[row][col] = "S"
                matrix[row + 1][col] = "."
                if food >= 10:
                    print(f"You won! You fed the snake.")
                    print(f"Food eaten: {food}")
                    flag = False
                    continue
            elif matrix[row][col] == "B":
                        matrix[row][col] = "."
                        matrix[row + 1][col] = "."
                        for i in range(len(matrix)):
                            for j in range(len(matrix[i])):
                                if matrix[i][j] == "B":
                                    row = i
                                    col = j
                                    matrix[row][col] = "S"

            else:
                matrix[row][col] = "S"
                matrix[row + 1][col] = "."

        else:
            matrix[row + 1][col] = "."
            print("Game over!")
            print(f"Food eaten: {food}")
            flag = False
            continue

    if comand == "down":
        s = matrix[row][col]
        row += 1
        if chek(row):
            if matrix[row][col] == "*":
                food += 1
                matrix[row][col] = "S"
                matrix[row - 1][col] = "."
                if food >= 10:
                    print(f"You won! You fed the snake.")
                    print(f"Food eaten: {food}")
                    flag = False
                    continue
            elif matrix[row][col] == "B":
                        matrix[row][col] = "."
                        matrix[row - 1][col] = "."
                        for i in range(len(matrix)):
                            for j in range(len(matrix[i])):
                                if matrix[i][j] == "B":
                                    row = i
                                    col = j
                                    matrix[row][col] = "S"
            else:
                matrix[row][col] = "S"
                matrix[row - 1][col] = "."


        else:
            matrix[row - 1][col] = "."
            print("Game over!")
            print(f"Food eaten: {food}")
            flag = False
            continue

    if comand == "left":
        s = matrix[row][col]
        col -= 1
        if chek(col):
            if matrix[row][col] == "*":
                food += 1
                matrix[row][col] = "S"
                matrix[row][col + 1] = "."
                if food >= 10:
                    print(f"You won! You fed the snake.")
                    print(f"Food eaten: {food}")
                    flag = False
                    continue
            elif matrix[row][col] == "B":
                    matrix[row][col] = "."
                    matrix[row][col + 1] = "."
                    for i in range(len(matrix)):
                        for j in range(len(matrix[i])):
                            if matrix[i][j] == "B":
                                    row = i
                                    col = j
                                    matrix[row][col] = "S"
            else:
                matrix[row][col] = "S"
                matrix[row][col + 1] = "."

        else:
            matrix[row][col + 1] = "."
            print("Game over!")
            print(f"Food eaten: {food}")
            flag = False
            continue

    if comand == "right":
        s = matrix[row][col]
        col += 1
        if chek(col):
            if matrix[row][col] == "*":
                food += 1
                matrix[row][col] = "S"
                matrix[row][col - 1] = "."
            elif food >= 10:
                    print(f"You won! You fed the snake.")
                    print(f"Food eaten: {food}")
                    flag = False
                    continue
            elif matrix[row][col] == "B":
                        matrix[row][col] = "."
                        matrix[row][col - 1] = "."
                        for i in range(len(matrix)):
                            for j in range(len(matrix[i])):
                                if matrix[i][j] == "B":
                                    row = i
                                    col = j
                                    matrix[row][col] = "S"

            else:
                matrix[row][col] = "S"
                matrix[row][col - 1] = "."


        else:
            matrix[row][col - 1] = "."
            print("Game over!")
            print(f"Food eaten: {food}")
            flag = False
            continue
    comand = input()
for i in matrix:

    print(''.join(i))