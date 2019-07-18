# 1.	一維串列的練習-max_min
# 事先將10個數字置於串列中，分別找出10個數字中最大的值和最小的值。
# (勿使用現成的函數)

import random


testnumber = [(random.randint(1, 12)) for i in range(10)]
print(testnumber)


def number_max(*number):
    num = number[0]
    for i in number:
        if i > num:
            num = i
    return num


def number_min(*number):
    num = number[0]
    for i in number:
        if i < num:
            num = i
    return num


print(number_max(*testnumber))
print(number_min(*testnumber))
