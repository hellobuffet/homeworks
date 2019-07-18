# 2.	選擇性敘述的練習-salary
# 輸入便利商店工讀生的工作時數，並計算其薪資。
# 60小時以內，時薪120元。
# 61~80小時，以時薪1.25倍計算。
# 81小時以上，以時薪1.5倍計算。
# 說明：薪資以累計方式計算。若工時為90小時，則薪資為60*120 + 20*120*1.25 + 10*120*1.5元。

worktime = eval(input('請輸入工時'))

print(type(worktime))
if worktime <= 60:
    salary = worktime * 120
elif 61 <= worktime <= 80:
    salary = (worktime - 60) * 120 * 1.25 + 7200
elif worktime > 81:
    salary = 7200 + 3000 + (worktime - 80) * 180
else:
    salary = 'fail'
print(salary)
