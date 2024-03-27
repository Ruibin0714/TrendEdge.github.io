import mysql.connector
import sys as s


con = mysql.connector.connect(

    user='root',
    password='12345678',
    host='localhost',
    database='mydb',


)
print('資料庫連線成功')
#建立cursor 物件







con.close()