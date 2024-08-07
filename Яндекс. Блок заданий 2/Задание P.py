player_1 = int(input())
player_2 = int(input())
player_3 = int(input())

name_1 = 'Петя'
name_2 = 'Вася'
name_3 = 'Толя'

if player_1 < player_2:
    player_1, player_2 = player_2, player_1
    name_1, name_2 = name_2, name_1
if player_1 < player_3:
    player_1, player_3 = player_3, player_1
    name_1, name_3 = name_3, name_1
if player_2 < player_3:
    player_2, player_3 = player_3, player_2
    name_2, name_3 = name_3, name_2

print(f'{name_1: ^24}')
print(f'{name_2: ^8}{" ": ^16}')
print(f'{" ": ^16}{name_3: ^8}')
print(f'{"II": ^8}{"I": ^8}{"III": ^8}')
