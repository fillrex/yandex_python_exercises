n = int(input())
sum = 0

for i in range(n):
    num = input()
    for digit in num:
        sum += int(digit)
    
print(sum)