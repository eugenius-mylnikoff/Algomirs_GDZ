vowels = ["a", "e", "i", "o", "u", "y"]

s = input()
count = 0
i = 0

while i < len(s) - 2:
    a, b, c = s[i], s[i + 1], s[i + 2]
    if a in vowels and b in vowels and c in vowels:
        count += 1
        i += 2
    elif a not in vowels and b not in vowels and c not in vowels:
        count += 1
        i += 2
    else:
        i += 1

print(count)