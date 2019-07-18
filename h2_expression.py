e = 0
for i in range(1, 51):
    if i % 2 == 0:
        e -= (i ** 2)
    else:
        e += (i ** 2)

print(e)
