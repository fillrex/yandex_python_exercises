a = float(input())
b = float(input())
c = float(input())

if a == b == c == 0:
    print('Infinite solutions')
elif a == 0 and b != 0 and c != 0:
    print(f'{-(c / b):.2f}')
elif a == b == 0:
    print('No solution')
elif a == c == 0:
    print('0.00')
else:
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        x_1 = (-b + discriminant ** 0.5) / (2 * a)
        x_2 = (-b - discriminant ** 0.5) / (2 * a)
        print(f'{min(x_1, x_2):.2f} {max(x_1, x_2):.2f}')
    elif discriminant == 0:
        x_1 = -b / (2 * a)
        print(round(x_1, 2))
    else:
        print('No solution')