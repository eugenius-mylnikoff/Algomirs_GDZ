k, T, S, N = map(int, input().split())
gold = 0
active_mines = 1
building_mines = []

for i in range(1, N + 1):
    gold += active_mines * k

    for j in range(len(building_mines)):
        if building_mines[j] != 0:
            building_mines[j] -= 1
        if building_mines[j] == 0:
            active_mines += 1
    building_mines = [el for el in building_mines if el != 0]

    if (N - i) > T and gold >= S:
        max_new_mines = gold // S
        building_mines.extend([T] * max_new_mines)
        gold -= max_new_mines * S

print(gold)