peter = int(input())
vasil = int(input())
tol = int(input())
if peter > vasil and peter > tol:
    print('Петя')
elif vasil > peter and vasil > tol:
    print('Вася')
elif tol > peter and tol > vasil:
    print('Толя')