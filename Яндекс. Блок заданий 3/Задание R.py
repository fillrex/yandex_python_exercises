n = int(input())

i = 2

while n > 1:
    while n % i == 0:
        n //= i
        if n != 1:
            print(i, end=' * ')
        else:
            print(i)
    i += 1