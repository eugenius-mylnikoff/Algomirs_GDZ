N, M = map(int, input().split())
arr = [list(map(int, input().split())) for j in range(N)]

max_area = 0
heights = [0] * M

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            heights[j] += 1
        else:
            heights[j] = 0

    for j in range(M):
        if heights[j] == 0:
            continue

        left = j
        while left > 0 and heights[left - 1] >= heights[j]:
            left -= 1

        right = j
        while right < M - 1 and heights[right + 1] >= heights[j]:
            right += 1

        width = right - left + 1
        area = width * heights[j]

        if area > max_area:
            max_area = area

print(max_area)