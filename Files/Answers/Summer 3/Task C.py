from itertools import product

K = int(input())
N = int(input())
weights = list(map(int, input().split()))

found = False

p = product([0, 1, 2], repeat=N)
for x in p:
    left = []
    right = []

    for i in range(N):
        if x[i] == 1:
            left.append(weights[i])
        elif x[i] == 2:
            right.append(weights[i])

    if K + sum(left) == sum(right):
        found = True

        if left:
            print(*left)
        else:
            print(0)

        if right:
            print(*right)
        else:
            print(0)

        break

if not found:
    print(-1)
