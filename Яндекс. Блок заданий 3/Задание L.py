n = int(input())
max, k = 0, 0

while n != 0:
    k = n % 10
    n = n // 10
    if k > max:
        max = k

print(max)