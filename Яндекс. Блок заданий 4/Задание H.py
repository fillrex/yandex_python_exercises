n = int(input())
sum = 0
max = 0

for _ in range(n):
    name = input()
    num = input()
    sum = 0
    for digit in num:
        sum += int(digit)
    if sum > max:
        max = sum
        max_name = name
    elif sum == max:
        max_name = name

print(max_name)