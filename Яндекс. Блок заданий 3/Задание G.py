a = int(input())
b = int(input())

c = a
d = b

while a > 0 and b > 0:
    if a >= b:
        a = a % b
    else:
        b = b % a

nod = max(a, b)
nok = c * d / nod
print(int(nok))