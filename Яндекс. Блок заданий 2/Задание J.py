n = int(input())

sum_1_2 = n // 100 + n // 10 % 10
sum_2_3 = n // 10 % 10 + n % 10

if sum_1_2 > sum_2_3:
    print(f'{sum_1_2}{sum_2_3}')
else:
    print(f'{sum_2_3}{sum_1_2}')