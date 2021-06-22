import math

n = int(input())

matrix = []

for i in range(n):
    matrix.append(input().split())


row = 0
col = 0
sum_p = 0

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        star = matrix[i][j]
        if star == "P":
            row = i
            col = j
            break
comand = input()
row_col = []
flag = True
coins = 0

while comand:

    if comand == "right":
        col += 1
        try:
            if matrix[row][col] == "X":
                coins = float(coins / 2)
                print(f"Game over! You've collected {math.floor(coins)} coins.")
                break
            else:
                coins += int(matrix[row][col])
                row_col.append([row,col])
            if coins >= 100:
                print(f"You won! You've collected {coins} coins.")
                break
        except:
            coins = float(coins / 2)
            print(f"Game over! You've collected {math.floor(coins)} coins.")
            break

    elif comand == "left":
        col -= 1
        try:
            if matrix[row][col] == "X":
                coins = float(coins / 2)
                print(f"Game over! You've collected {math.floor(coins)} coins.")
                break
            else:
                coins += int(matrix[row][col])
                row_col.append([row, col])
            if coins >= 100:
                print(f"You won! You've collected {coins} coins.")
                break
        except:
            coins = float(coins / 2)
            print(f"Game over! You've collected {math.floor(coins)} coins.")
            break

    elif comand == "up":
        row -= 1
        try:
            if matrix[row][col] == "X":
                coins = float(coins / 2)
                print(f"Game over! You've collected {math.floor(coins)} coins.")
                break
            else:
                coins += int(matrix[row][col])
                row_col.append([row, col])
            if coins >= 100:
                print(f"You won! You've collected {coins} coins.")
                break
        except:
            coins = float(coins / 2)
            print(f"Game over! You've collected {math.floor(coins)} coins.")
            break

    elif comand == "down":
        row += 1
        try:
            if matrix[row][col] == "X":
                coins = float(coins / 2)
                print(f"Game over! You've collected {math.floor(coins)} coins.")
                break
            else:
                coins += int(matrix[row][col])
                row_col.append([row, col])
            if coins >= 100:
                print(f"You won! You've collected {coins} coins.")
                break
        except:
            coins =float(coins / 2)
            print(f"Game over! You've collected {math.floor(coins)} coins.")
            break

    comand = input()

print("Your path:")
for i in range(len(row_col)):
    print(row_col[i])