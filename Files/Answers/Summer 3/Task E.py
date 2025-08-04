import string

s = input()
K = int(input())
alphabet = string.ascii_uppercase
result = ""
for el in s:
    id = alphabet.index(el) - K
    result += alphabet[id]
print(result)
