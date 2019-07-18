tag = 10000
k = 0
lis = []

for ma in range(tag):
    # ma_s = str(ma)
    for i in str(ma):
        k = k + int(i) ** 3
    if ma == k:
        lis.append(k)
    k = 0
print(lis)
