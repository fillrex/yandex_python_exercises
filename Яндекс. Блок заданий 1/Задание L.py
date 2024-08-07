m = int(input())
n = int(input())
m1 = m // 100
m2 = m // 10 % 10
m3 = m % 10
n1 = n // 100
n2 = n // 10 % 10
n3 = n % 10
res1 = (m1 + n1) % 10
res2 = (m2 + n2) % 10
res3 = (m3 + n3) % 10
result = f'{str(res1)}{str(res2)}{str(res3)}'
print(result)