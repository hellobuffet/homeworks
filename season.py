# # 1.	選擇性敘述的練習-season
# # 輸入月份1~12月，判斷相對應的季節春、夏、秋、冬並印出。若不在此範圍則印出”輸入錯誤”。
# season = eval(input('請輸入月份：'))
#
# if 1 <= season <= 2:
#     print("冬季")
# elif 3 <= season <= 5:
#     print("春季")
# elif 6 <= season <= 8:
#     print("夏季")
# elif 9 <= season <= 11:
#     print("秋季")
# elif season == 12:
#     print("冬季")
# else:
#     print("輸入錯誤")


for season in range(0, 12, 1):
    print(season)
    if 1 <= season <= 2:
        print("冬季")
    elif 3 <= season <= 5:
        print("春季")
    elif 6 <= season <= 8:
        print("夏季")
    elif 9 <= season <= 11:
        print("秋季")
    elif season == 12:
        print("冬季")
    else:
        print("輸入錯誤")
