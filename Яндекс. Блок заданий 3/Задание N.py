n = int(input())

simple = True

if n <= 1:
    simple = False
else:
    for div in range(2, int(n ** 0.5 + 1)):
        if n % div == 0:
            simple = False
            break

if simple is True:
    print('YES')
else:
    print('NO')