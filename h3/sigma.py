# 1.	函數的練習-sigma
from math import factorial


def my_fun(x, n):
    total = 0
    for i in range(n + 1):

        total += ((x ** i) / (factorial(i)))
    return total


def main():
    print(my_fun(5, 3))


main()
