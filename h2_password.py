for i in range(3):
    s = input("請輸入密碼：")
    if s == 'password':
        break

if i == 2:
    print('輸入密碼超過三次')
else:
    print("歡迎使用本系統")
