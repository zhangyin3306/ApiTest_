import pymysql
from utils.LogUtil import my_log
class mysqlutil:
    def __init__(self,host,user,password,database):
        self.log = my_log()
        self.conn = pymysql.connect(
        host = host,
        user= user,
        password = password,
        database= database
        )
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
    def fetchone(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def fetchall(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def exec(self, sql):
        """
        执行
        :return:
        """
        try:
            if self.conn and self.cursor:
                self.cursor.execute(sql)
                self.conn.commit()
        except Exception as ex:
                self.conn.rollback()
                self.log.error("Mysql 执行失败")
                self.log.error(ex)
                return False
        return True

    # 4、关闭对象
    def __del__(self):
        # 关闭光标对象
        if self.cursor is not None:
            self.cursor.close()
        # 关闭连接对象
        if self.conn is not None:
            self.cursor.close()



