number = int(input())

n_1 = number // 100
n_2 = number // 10 % 10
n_3 = number % 10

if n_1 == max(n_1, n_2, n_3):  # n_1 - max
    if n_2 == min(n_2, n_3):  # n_2 - min
        if n_1 + n_2 == n_3 * 2:
            print('YES')
        else:
            print('NO')
    else:  # n_3 - min
        if n_1 + n_3 == n_2 * 2:
            print('YES')
        else:
            print('NO')
elif n_2 == max(n_1, n_2, n_3):  # n_2 - max
    if n_1 == min(n_1, n_3):  # n_1 - min
        if n_2 + n_1 == n_3 * 2:
            print('YES')
        else:
            print('NO')
    else:  # n_3 - min
        if n_2 + n_3 == n_1 * 2:
            print('YES')
        else:
            print('NO')
elif n_3 == max(n_1, n_2, n_3):  # n_3 - max
    if n_1 == min(n_1, n_2):  # n_1 - min
        if n_3 + n_1 == n_2 * 2:
            print('YES')
        else:
            print('NO')
    else:  # n_2 - min
        if n_3 + n_2 == n_1 * 2:
            print('YES')
        else:
            print('NO')