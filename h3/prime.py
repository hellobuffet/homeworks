# 3.	函數的練習-prime
# 寫一函數get_prime (n)用來找出第n個質數。



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


def get_prime(num):
    j = 0
    i = 1
    while i <= num:
        j = j + 1
        if is_prime(j)[1] == '是質數':
            i = i + 1
        # print(j,is_prime(j))

    return is_prime(j)
    # print(j)


def main():
    x=5
    print('第', x, '個質數是', get_prime(x)[0])


main()
