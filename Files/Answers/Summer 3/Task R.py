n = int(input())
arr = list(map(int, input().split()))

max_sum = arr[0]
current_sum = arr[0]
start = 1
end = 1
result_start = 1
result_end = 1

for i in range(1, n):
    if current_sum < 0:
        current_sum = arr[i]
        start = i + 1
        end = i + 1
    else:
        current_sum += arr[i]
        end = i + 1

    if current_sum > max_sum:
        max_sum = current_sum
        result_start = start
        result_end = end

print(result_start, result_end, max_sum)
