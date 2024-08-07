n_1 = int(input())
n_2 = int(input())

a = n_1 // 10
b = n_1 % 10
c = n_2 // 10
d = n_2 % 10

max_n = max(a, b, c, d)
min_n = min(a, b, c, d)
sum = a + b + c + d
mean = (sum - max_n - min_n) % 10

print(f'{max_n}{mean}{min_n}')