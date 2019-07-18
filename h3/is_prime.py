# 2.	函數的練習-is_prime
# 寫一函數is_prime(n)用來判斷n是否為質數。

def is_prime(num):
    number_list = []
    for i in range(1, num + 1):
        if num % i == 0:
            number_list.append(i)
            # print(i, j)

    if len(number_list) <= 2 and num != 1:
        return i, '是質數'
    else:
        return i, '不是質數'


def main():
    x = is_prime(100)
    print(x[0])
    print(x[1])


main()
