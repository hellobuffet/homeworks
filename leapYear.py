year = eval(input())
if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 and year % 3200 != 0)):
    print("閏年")
else:
    print("平年")
