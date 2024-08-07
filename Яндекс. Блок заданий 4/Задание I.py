n = int(input())
total_max = ''

for _ in range(n):
    num = int(input())
    max = 0
    while num != 0:
        current_n = num % 10
        if current_n > max:
            max = current_n
        num //= 10
    total_max += str(max)

print(total_max)
        