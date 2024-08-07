number = int(input())

x = number // 100
y = number // 10 % 10
z = number % 10

xy = f'{x}{y}'
xz = f'{x}{z}'
yx = f'{y}{x}'
yz = f'{y}{z}'
zx = f'{z}{x}'
zy = f'{z}{y}'

if y == 0:
    n_min = min(xy, xz, zx, zy)
    n_max = max(xy, xz, zx, zy)
elif z == 0:
    n_min = min(xy, xz, yx, yz)
    n_max = max(xy, xz, yx, yz)
else:
    n_min = min(xy, xz, yx, yz, zx, zy)
    n_max = max(xy, xz, yx, yz, zx, zy)

print(n_min, n_max)