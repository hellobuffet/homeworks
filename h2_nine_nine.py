row = 0
col = 9
for row in range(9, 0, -1):
    print(row, '｜', end='')
    for col in range(1, 10):
        if row == col:
            print(row * col)
            break
        else:
            print(row * col, end='　')
