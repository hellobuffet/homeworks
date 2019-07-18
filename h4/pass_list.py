list_test = [[75, 52, 90, 39], [56, 22, 34, 53], [80, 85, 46, 93]]
avg_list = []


def com_avg(*list_test):
    avg_list = []
    num = 0
    for i in list_test:
        for j in i:
            num += int(j)

    num = num / (len(list_test) * len(i))
    return num


def find_max(*list_test):
    find_min_list = []
    num = 0
    for i in list_test:
        for j in i:
            find_min_list.append(j)
            num += j
    num = (num / len(find_min_list))
    for i in find_min_list:
        if i > num:
            num = i
    return num


def find_min(*list_test):
    find_min_list = []
    num = 0
    for i in list_test:
        for j in i:
            find_min_list.append(j)
            num += j
    num = (num / len(find_min_list))
    for i in find_min_list:
        if i < num:
            num = i
    return num


def com_4_avg(*list_test):
    avg_list = []
    num = 0
    for i in list_test:
        for j in i:
            num += int(j)

        avg_list.append(int(num / len(i)))

    return avg_list


print(com_avg(*list_test))
print(find_max(*list_test))
print(find_min(*list_test))
print(com_4_avg(*list_test))
