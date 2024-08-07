i = 0
while (name := input()) != 'Приехали!':
    if 'зайка' in name:
        i += 1
print(i)