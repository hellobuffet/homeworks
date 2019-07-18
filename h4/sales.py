price = [12, 16, 10, 14, 15]
amount = [[33, 32, 56, 45, 33],
          [77, 33, 68, 45, 23],
          [43, 55, 43, 67, 65]]
product = ['A', 'B', 'C', 'D', 'E']
salesMan = ['Jean', 'Tom', 'Tina']


def everyone_sales(price, amount, salesMan):
    total_sales = 0
    total_sales_list = []
    for i in range(len(salesMan)):
        for j in range(len(price)):
            total_sales = total_sales + (price[j] * amount[i][j])
        total_sales_list.append([salesMan[i], total_sales])
        total_sales = 0
    return total_sales_list


def max_salesman(price, amount, salesMan):
    total_sales_list = everyone_sales(price, amount, salesMan)
    max_price = total_sales_list[0][1]
    max_salesman = ''
    for i in range(len(total_sales_list)):
        if total_sales_list[i][1] >= max_price:
            max_price = total_sales_list[i][1]
            max_salesman = total_sales_list[i][0]
    return max_salesman


def everyone_product_sales(price, amount, product):
    total_sales = 0
    total_sales_list = []
    for i in range(len(product)):
        for j in range(len(amount)):
            total_sales = total_sales + (price[i] * amount[j][i])
        total_sales_list.append([product[i], total_sales])
    return total_sales_list


def max_sales_product(price, amount, product):
    max_sales_product = everyone_product_sales(price, amount, product)
    max_price = max_sales_product[0][1]
    max_product = ''
    for i in range(len(max_sales_product)):
        if max_sales_product[i][1] >= max_price:
            max_price = max_sales_product[i][1]
            max_product = max_sales_product[i][0]
    return max_product


def main():
    print(everyone_sales(price, amount, salesMan))
    print(max_salesman(price, amount, salesMan))
    print(everyone_product_sales(price, amount, product))
    print(max_sales_product(price, amount, product))


main()


