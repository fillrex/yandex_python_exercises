n = int(input())
a = n // 1000
b = n // 100 % 10
c = n // 10 % 10
d = n % 10
badc = int(str(b) + str(a) + str(d) + str(c))
print(badc)