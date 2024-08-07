sum = 0
while (name := float(input())) != 0:
    if name >= 500:
        name *= 0.9
        sum += name
    else:
        sum += name
print(sum)