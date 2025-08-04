a = [int(i) for i in input().split()]
count = 0
maximum = 0
now = 0
result = 0
for i in range(len(a)):
    count = 0
    now = a[i]
    for s in a:
        if s == now:
            count += 1
    if count > maximum:
        maximum = count
        result = now
print(result)