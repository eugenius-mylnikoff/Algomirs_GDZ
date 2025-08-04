arr = []
a = 1
while a != 0:
    a = int(input())
    if a != 0:
        arr.append(a)
indexes = []
for i in range(1, len(arr) - 1):
    if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
        indexes.append(i)
if len(indexes) >= 2:
    min_distance = 10 ** 10
    for i in range(1, len(indexes)):
        distance = indexes[i] - indexes[i - 1]
        min_distance = min(min_distance, distance)
    print(min_distance)
else:
    print(0)
