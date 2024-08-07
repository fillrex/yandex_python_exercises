n = int(input())
count = 0

for _ in range(n):
    num = int(input())
    if num // 10 == 0:
        count += 1
        continue
    original_num = num
    current_n = 0
    reversed_num = ''
    while num != 0:
        current_n = num % 10
        reversed_num += str(current_n)
        num //= 10
    if int(reversed_num) == original_num:
        count += 1

print(count)