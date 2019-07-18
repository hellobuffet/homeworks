perf = 0
x = 1000
for i in range(1, x + 1):
    # 跑1到100
    for j in range(1, i):
        if i % j == 0:
            # print(i, j)
            # print('加總前', perf)
            perf += j
            # print('加總後', perf)

    if i == perf:
          print('完美數：',perf)
    perf = 0
    # print(i,perf)
    #
    # if perf == i:
    #     print(perf)
