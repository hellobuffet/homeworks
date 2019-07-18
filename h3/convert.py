num = 0

str1 = 123


def to_binary(n):
    i = n
    bin_list = []
    tagnum = ''
    while i > 0:
        bin_list.append(str(i % 2))

        i = i // 2

    bin_list.reverse()
    for i in bin_list:
        tagnum += i
    return tagnum


def to_hexadecimal(n):
    i = n
    bin_list = []
    tagnum = ''
    dis = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    while i > 0:

        bin_list.append(dis[(i % 16)])
        # print(dis[i % 16])
        i = i // 16
        # print(i)

    bin_list.reverse()
    for i in bin_list:
        tagnum += i
    return tagnum


print(to_binary(str1))
print(to_hexadecimal(str1))
