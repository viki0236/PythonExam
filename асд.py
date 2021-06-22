max_num = int(input())
row = []
for triangle in range(max_num):
    row.append(triangle + 1)
    print(*row)
for r in range(len(row)):
    row.pop(-1)
    print(*row)
