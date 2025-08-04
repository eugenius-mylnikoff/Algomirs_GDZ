K, M = map(int, input().split())

max_val = 0

if K == 1:
    max_val = 0
elif K > M:
    max_val = M
elif K < M:
    max_val = K
elif K == M:
    max_val = M

print(max_val)
