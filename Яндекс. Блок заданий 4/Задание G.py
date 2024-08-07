n = int(input())
time = 3

for i in range(1, n + 1):
    for j in range(time, 0, -1):
        print(f'До старта {j} секунд(ы)')
    print(f'Старт {i}!!!')
    time += 1