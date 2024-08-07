name_1 = input()
name_2 = input()
name_3 = input()

if name_1 < name_2 and name_1 < name_3:
    print(name_1)
elif name_2 < name_1 and name_2 < name_3:
    print(name_2)
elif name_3 < name_1 and name_3 < name_2:
    print(name_3)