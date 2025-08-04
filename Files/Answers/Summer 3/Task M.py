A = int(input())
B, C = 0, 0
max_sum = 0
for i, j in zip(range(A), range(A, -1, -1)):
    sum_B = sum(list(int(el) for el in str(i)))
    sum_C = sum(list(int(el) for el in str(j)))
    summa = sum_B + sum_C
    if summa > max_sum:
        max_sum = summa
        B, C = i, j
print(max_sum)
print(B, C)
