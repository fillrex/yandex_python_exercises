k = int(input())
n = int(input())

i = 0

if k < n:
    for i in range(k, n + 1):
        print(i, end=' ')
else:
    for i in range(k, n - 1, -1):
        print(i, end=' ')