# 1.	檔案的練習-dump_emp
# 將employee表格裡的所有資料dump至檔案中。
# 註：一筆資料一列，每個資料欄的資料以逗號(,)隔開

import mysql.connector
from mysql.connector import errorcode

conn = None
config = {'database': 'db01',
          'user': 'root',
          'password': 'QAqa9221462069'}
try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    select = "select empno, ename, hiredate, salary, deptno, title  from employee"
    cursor.execute(select)
    emps = cursor.fetchall()
    employee_list = []
    with open('employee_list.txt', 'w') as f:
            f.write('')
    for empno, ename, hiredate, salary, deptno, title in emps:
        with open('employee_list.txt', 'a') as f:
            f.write("{},{},{},{},{},{}".format(empno, ename, hiredate, salary, deptno, title))
            f.write('\n')

    # conn.commit()
    # print(cursor)
    # for empno, ename, hiredate, salary, deptno, title in cursor:
    #     print("empno={}, ename={}, hiredate={}, salary={}, deptno={}, title={}".format(empno, ename, hiredate, salary,
    #                                                                                    deptno, title))

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
