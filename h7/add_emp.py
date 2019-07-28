# 2.	檔案的練習-add_emp
# 在emp.txt文字檔中設定五筆employee的資料，將之新增至資料庫中。
# 註1：一筆資料一列，每個資料欄的資料以逗號(,)隔開
# 註2：建議使用cursor.executemany(sql, seq_of_params)來實作


import mysql.connector
from mysql.connector import errorcode

emp_list = []
with open('emp.txt', 'r')as f:
    for i in f:
        i = i[: -2]
        i = i.split(',')
        emp_list.append(tuple(i))

print(emp_list)

conn = None
config = {'database': 'db01',
          'user': 'root',
          'password': 'QAqa9221462069'}
try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    upd = "inter into employee VALUES(%s,%s,%s,%s,%s,%s)"
    cursor.execute(upd, tuple(emp_list))
    conn.commit()
    print('insert', cursor.rowcount, "employees")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("user or password error")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("database doesn't existed")
    else:
        print(err)
finally:
    if cursor:
        cursor.close()
    if conn:
        print('data is closed')
        conn.close()