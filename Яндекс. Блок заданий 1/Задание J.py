name = input()
number = int(input())
group_number = number // 100
bed_number = number // 10 % 10
list_number = number % 10
print(f'Группа №{group_number}.\n{list_number}. {name}.\nШкафчик: {number}.\nКроватка: {bed_number}.')