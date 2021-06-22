from collections import deque

bomb_effect = deque(input().split(", "))
bom_casing = input().split(", ")

datura_bombs = 0
cherry_bombs = 0
smoke_decoy_bombs = 0

while len(bomb_effect) > 0 and len(bom_casing) > 0 :
    b_efect = int(bomb_effect.popleft())
    b_casing = int(bom_casing.pop())
    flag = True
    while flag:
        result = b_efect + b_casing
        if result == 40:
            datura_bombs += 1
            flag = False
        elif result == 60:
            cherry_bombs += 1
            flag = False
        elif result == 120:
            smoke_decoy_bombs += 1
            flag = False
        else:
            b_casing = b_casing - 5
    if datura_bombs >= 3 and cherry_bombs >= 3 and smoke_decoy_bombs >= 3:
        break

if datura_bombs >= 3 and cherry_bombs >= 3  and smoke_decoy_bombs >= 3:
    print(f"Bene! You have successfully filled the bomb pouch!")
    if len(bomb_effect) > 0:
        print(f"Bomb Effects: {', '.join(bomb_effect)}")
    else:
        print("Bomb Effects: empty")
    if len(bom_casing) > 0:
        print(f"Bomb Casings: {', '.join(bom_casing)}")
    else:
        print("Bomb Casings: empty")
    print(f"Cherry Bombs: {cherry_bombs}")
    print(f"Datura Bombs: {datura_bombs}")
    print(f"Smoke Decoy Bombs: {smoke_decoy_bombs}")
else:
    print("You don't have enough materials to fill the bomb pouch.")
    if len(bomb_effect) > 0:
        print(f"Bomb Effects: {', '.join(bomb_effect)}")
    else:
        print("Bomb Effects: empty")
    if len(bom_casing) > 0:
        print(f"Bomb Casings: {', '.join(bom_casing)}")
    else:
        print("Bomb Casings: empty")
    print(f"Cherry Bombs: {cherry_bombs}")
    print(f"Datura Bombs: {datura_bombs}")
    print(f"Smoke Decoy Bombs: {smoke_decoy_bombs}")