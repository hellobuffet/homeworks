import random

id_dict = {'A': 1, 'B': 10, 'C': 19, 'D': 28, 'E': 37, 'F': 46, 'G': 55, 'H': 64, 'I'
: 39, 'J': 73, 'K': 82, 'M': 11, 'N': 20, 'O': 48, 'P': 29, 'Q': 38, 'T': 65, 'U': 74, 'V': 83, 'W': 21, 'X': 3,
           'Z': 30, '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

county_dict = {'臺北市': 'A', '臺中市': 'B', '基隆市': 'C', '臺南市': 'D', '高雄市': 'E', '新北市': 'F', '宜蘭縣': 'G', '桃園市': 'H',
               '嘉義市': 'I',
               '新竹縣': 'J', '苗栗縣': 'K', '南投縣': 'M', '彰化縣': 'N', '新竹市': 'O', '雲林縣': 'P', '嘉義縣': 'Q', '屏東縣': 'T',
               '花蓮縣': 'U',
               '臺東縣': 'V', '金門縣': 'W', '澎湖縣': 'X', '連江縣': 'Z'}

# county = str(input("請輸入要縣市代碼："
#                    "'臺北市': 'A', "
#                    "'臺中市': 'B', "
#                    "'基隆市': 'C', "
#                    "'臺南市': 'D', "
#                    "'高雄市': 'E', "
#                    "'新北市': 'F', "
#                    "'宜蘭縣': 'G', "
#                    "'桃園市': 'H', "
#                    "'嘉義市': 'I', "
#                    "'新竹縣': 'J', "
#                    "'苗栗縣': 'K', "
#                    "'南投縣': 'M', "
#                    "'彰化縣': 'N', "
#                    "'新竹市': 'O', "
#                    "'雲林縣': 'P', "
#                    "'嘉義縣': 'Q', "
#                    "'屏東縣': 'T',"
#                    "'花蓮縣': 'U',"
#                    "'臺東縣': 'V', "
#                    "'金門縣': 'W', "
#                    "'澎湖縣': 'X', "
#                    "'連江縣': 'Z'"))
# gender = str(input('請輸入性別(男性輸入1，女性輸入2)：'))

county = 'A'
gender = '2'

def id_generator(county, gender):
    id_list = [county, int(gender), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9),
               random.randint(0, 9),
               random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)]
    end_number = ((id_dict[id_list[0]] + int(gender) * 8 + id_list[2] * 7 + id_list[3] * 6 + id_list[4] * 5 + id_list[
        5] * 4 + id_list[6] * 3 + id_list[7] * 2 + id_list[8]) % 10)
    if end_number != 0:
        end_number = 10 - end_number

    id_list.append(end_number)
    id_number = ''
    for i in id_list:
        id_number += str(i)

    return id_number


def main():
    print(id_generator(county, gender))

main()