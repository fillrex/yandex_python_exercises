n = int(input())

res = 0
power = 1

while n != 0:
    if n % 2 != 0:
        res += (n % 10) * power
        power *= 10
    n //= 10

print(res)

