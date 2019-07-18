def is_mersenne_prime(n):
    flag = 1
    prime_count = 1
    prime_number = 0
    number_list = []
    prime_list = []
    while flag <= n:
        prime_number = (2 ** prime_count) - 1
        if is_prime(prime_number)[1] == '是質數':
            prime_list.append(prime_number)
            flag += 1
            prime_count += 1
        else:
            prime_count += 1

    return prime_list


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


print(is_mersenne_prime(5))
