# 3.	選擇性敘述的練習-electricity
# 輸入何種用電和度數，計算出需繳之電費。
# 電力公司使用累計方式來計算電費，分工業用電及家庭用電。
#                    	   家庭用電        工業用電
#    240度(含)以下			0.15元			0.45元
#    240~540(含)度   		0.25元			0.45元
#    540度以上        	0.45元			0.45元

electricity_type = input("家庭用電輸入1，工業用電輸入2")
electricity_number = eval(input("請輸入本月電力"))
electricity_fee = 0
if electricity_type == '1':
    if 0 <= electricity_number <= 240:
        electricity_fee = electricity_number * 0.15
    elif 240 <= electricity_number <= 540:
        electricity_fee = electricity_number * 0.25
    elif electricity_number > 540:
        electricity_fee = electricity_number * 0.45
    else:
        electricity_fee = '輸入錯誤'
elif electricity_type == '2':
    electricity_fee = electricity_number * 0.45
else:
    print('輸入錯誤')

print(electricity_fee)
