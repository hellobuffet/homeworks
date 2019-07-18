target_id = 'JJJJJJJJJJ'
check_id = 0
check_id_list = []
check_id_mod_list = [1, 8, 7, 6, 5, 4, 3, 2, 1, 1]
id_dict = {'A': 1, 'B': 10, 'C': 19, 'D': 28, 'E': 37, 'F': 46, 'G': 55, 'H': 64, 'I'
: 39, 'J': 73, 'K': 82, 'M': 11, 'N': 20, 'O': 48, 'P': 29, 'Q': 38, 'T': 65, 'U': 74, 'V': 83, 'W': 21, 'X': 3,
           'Z': 30, '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def check_id(target_id):
    if len(target_id) == 10:
        for i in target_id:
            check_id_list.append(i)

        if check_id_list[1] == '1' or check_id_list[1] == '2':
            num = 0
            j = 0
            for i in check_id_list:
                num += (id_dict[i] * check_id_mod_list[j])
                # print(id_dict[i], ' X ', check_id_mod_list[j], ' = ', num)
                j += 1

            if num % 10 == 0:
                print(target_id, '是正確身分證')
                return (target_id, '是正確身分證')

    # print(target_id, '不是正確身分證')
    return (target_id, '不是正確身分證')


def main():
    target_id = 'J1JJJJJJJJ'
    print(check_id(target_id))


main()
