import pymysql
import pytest


conn = pymysql.connect(
    host= 'rm-bp1mtvx6w7igg28e9.mysql.rds.aliyuncs.com',
    user= 'shangfu_charge',
    password= '2Ote#v5PfoVsQniw',
    database= 'shangfu_charge'
)

# 获取执行SQL语句的光标对象
cursor = conn.cursor() # 结果集默认以元组显示
cursor.execute("select * from cm_a_pile")
# 执行
data = cursor.fetchone()
print("Database version:", data)

# 关闭光标对象
cursor.close()
# 关闭数据库连接
conn.close()


