peter = int(input())
vasil = int(input())
tol = int(input())

if peter > vasil and peter > tol:  # 1. Петя
    if vasil > tol:  # 1. Петя 2. Вася 3. Толя
        print(f'1. Петя\n2. Вася\n3. Толя')
    else:
        print(f'1. Петя\n2. Толя\n3. Вася')  # 1. Петя 2. Толя 3. Вася
elif vasil > peter and vasil > tol:  # 1. Вася
    if peter > tol:  # 1. Вася 2. Петя 3. Толя
        print(f'1. Вася\n2. Петя\n3. Толя')
    else:  # 1. Вася 2. Толя 3. Петя
        print(f'1. Вася\n2. Толя\n3. Петя')
elif tol > peter and tol > vasil:  # 1. Толя
    if peter > vasil:  # 1. Толя 2. Петя 3. Вася
        print(f'1. Толя\n2. Петя\n3. Вася')
    else:  # 1. Толя 2. Вася 3. Петя
        print(f'1. Толя\n2. Вася\n3. Петя')
