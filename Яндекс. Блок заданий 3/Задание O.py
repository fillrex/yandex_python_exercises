n = int(input())
c = 0

for i in range(n):
    if 'зайка' in (string := input()):
        c += 1

print(c)