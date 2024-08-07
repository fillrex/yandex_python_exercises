n = int(input())
min = input()

for i in range(n - 1):
    name = input()
    if name < min:
        min = name

print(min)