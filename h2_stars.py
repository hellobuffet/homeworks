for i in range(5):
    for j in range(i + 1):
        print("＊", end='')
    print()

i = 0
j = 0

for i in range(5):
    for j in range(i + 1):
        print("　", end='')

    for k in range(5-i):
        print("＊", end='')

    print('')
i=0
j=0
k=0

for i in range(5):
    for j in range(i + 1):
        print("　", end='')

    for k in range(5-i):
        print("＊　", end='')

    print('')

for i in range(5):
    for k in range(5-i):
        print("　", end='')

    for j in range(i + 1):
        print("＊　", end='')

    print('')

    