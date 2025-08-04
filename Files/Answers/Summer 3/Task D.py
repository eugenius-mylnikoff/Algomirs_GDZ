N = int(input())
arr = list(map(int, input().split()))
result = 0
for i in range(N - 1):
    if arr[i] + 1 != arr[i + 1]:
        result += 1
print(result)
