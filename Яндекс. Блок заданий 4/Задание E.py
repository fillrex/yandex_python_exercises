n = int(input())
string = ''
count = 0
has_hare = False

for _ in range(n):
    while string != 'ВСЁ':
        string = input()
        if 'зайка' in string:
            has_hare = True
    if has_hare:
        count += 1
        has_hare = False
    string = ''

print(count)