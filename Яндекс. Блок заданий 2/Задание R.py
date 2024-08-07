first = int(input())
second = int(input())
third = int(input())

sum = first + second + third
c = max(first, second, third)
a = min(first, second, third)
b = sum - a - c

if a ** 2 + b ** 2 == c ** 2:
    print('100%')
elif a ** 2 + b ** 2 > c ** 2:
    print('крайне мала')
else:
    print('велика')