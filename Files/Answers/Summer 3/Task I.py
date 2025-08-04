def kthdigit(n):
    s = str(n)
    if len(s) >= k:
        return int(s[k - 1])
    else:
        return 0


k = int(input())
s = list(map(int, input().split()))
s.sort(key=kthdigit)
print(" ".join(map(str, s)))
