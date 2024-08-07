x, y = 0, 0
while (axis := input()) != 'СТОП':
    step = int(input())
    if axis == 'ВОСТОК':
        x += step
    elif axis == 'ЗАПАД':
        x -= step
    elif axis == 'СЕВЕР':
        y += step
    elif axis == 'ЮГ':
        y -= step

print(y)
print(x)