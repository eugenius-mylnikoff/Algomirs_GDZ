K = int(input())
s = input()
N = len(s)
count = 0

for i in range(N - K + 1):
    pattern = s[i:i + K]
    pos = i + K
    operations = 0
    pattern_pos = 0

    while pos < N:
        if s[pos] == pattern[pattern_pos % K]:
            operations += 1
            pos += 1
            pattern_pos += 1
        else:
            break

    if operations >= 1:
        count += operations

print(count)
