n = int(input())
m = ''
k = n
while n != 0:
    m += str(n % 10)
    n //= 10

if k == int(m):
    print('YES')
else:
    print('NO')