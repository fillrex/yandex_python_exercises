n = int(input())

n_reversed = int(str(n % 10) + str(n // 10 % 10) + str(n // 100 % 10) + str(n // 1000))

if n == n_reversed:
    print('YES')
else:
    print('NO')