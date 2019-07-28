# 6.	選擇性敘述的練習-equation
# 一元二次方程式ax2+bx+c=0。輸入a, b, c三值，並計算方程式的根。
# b2-4ac > 0，有兩個不相等的實根。
# b2-4ac = 0，有兩個相等的實根。
# b2-4ac < 0，則印出”沒有實根”。


a = 3
b = 40
c = 5
root = (b ** 2) - 4 * a * c

if root > 0:
    print("有兩個不相等的實根")
    print("實跟1：{}，實跟2：{}".format((-b + root) / (2 * a), (-b - root) / (2 * a)))
elif root == 0:
    print("有兩個相等的實根")
    print("".format((-b)/(2*a)))
elif root < 0:
    print("沒有實根")
