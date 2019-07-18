import random


def rain_random():
    rain1 = []
    rain2 = []
    rain3 = []
    for i in range(1, 6):
        for j in range(1, 5):
            for k in range(1, 4):
                rain1.append(random.randint(10, 1000))
            rain2.append(rain1)
            rain1 = []
        rain3.append(rain2)
        rain2 = []
    return rain3


def enter_want_type():
    try:
        num = str(input("請輸入all year season month："))
        if "all" in num or "year" in num:
            if "all" in num:
                calculation_all_rain_avg()
            elif "year" in num and "season" in num:
                calculation_year_season_rain_avg()
            elif "year" in num and "month" in num:
                calculation_year_month_rain_avg()
            elif "year" in num:
                calculation_year_rain_avg()
        else:
            raise ValueError
    except ValueError:
        print("輸入錯誤")


def calculation_all_rain_avg():
    print("all")


def calculation_year_rain_avg():
    print("year")


def calculation_year_season_rain_avg():
    print("yearseason")


def calculation_year_month_rain_avg():
    print("yearmonth")


def enter_select():
    pass


enter_want_type()
