tag_number = 23
number_list = []
prime_list = []
for i in range(2, tag_number+1):
    # print(i, '==========')
    for j in range(2, i):
        if i % j == 0:
            number_list.append(j)
            # print(i, j)

    if len(number_list) <= 1:
        prime_list.append(i)
        # print(prime_list)

    number_list = []

print(prime_list)
