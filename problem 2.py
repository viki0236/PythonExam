p_1, p_2 = input().split(", ")
# pleyar = {}
# for n in name:
#     pleyar[n] = int(501)
p_1 = 501
p_2 = 501

matrix = []
for i in range(7):
    matrix.append([x for x in input().split()])

nums = input()

n = int(nums[1])
m = int(nums[4])
print(matrix[n][-1])
counter = 0
while nums:

    if matrix[n][m] == "T":
        tochki = int(matrix[n][0]) + int(matrix[n][-1]) + int(matrix[0][m]) + int(matrix[-1][m])
        tochki = tochki * 2

        if counter % 2 == 0:
            p_1 -= tochki
        else:
            p_2 -= tochki

    elif matrix[n][m] == "D":

        tochki = matrix[n][0] + matrix[n][-1] + matrix[0][m] + matrix[-1][m]
        tochki = tochki * 2

        if counter % 2 == 0:
            p_1 -= tochki
        else:
            p_2 -= tochki

    elif matrix[n][m] == "B":

        if counter % 2 == 0:
            print(f"{p_1} won the game with {counter} throws!")
        else:
            print(f"{p_2} won the game with {counter} throws!")