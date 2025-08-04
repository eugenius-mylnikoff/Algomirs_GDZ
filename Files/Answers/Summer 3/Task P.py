n = int(input())
k_min = (n + 5) // 6
k_max = n
min_score = 7 * k_min - n
max_score = 7 * k_max - n
print(min_score, max_score)