bottles = [int(input()) for i in range(10)]
srednee = sum(bottles) // len(bottles)
if all(el == srednee for el in bottles):
    print(0)
else:
    result = sum(1 for el in bottles if el > srednee)
    print(result)
