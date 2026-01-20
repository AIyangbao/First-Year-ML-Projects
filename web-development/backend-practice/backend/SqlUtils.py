import pymysql
class SqlUtil:
    # 初始化函数(创建类对象时这个函数会自动被调用执行)  用这个函数接收实例化类对象时传递进来的参数
    def __init__(self,_host,_port,_user,_password,_database):
        self.host=_host
        self.port=_port
        self.user=_user
        self.password=_password
        self.database=_database

    # 获取连接对象
    def getconnect(self):
        return pymysql.connect(host=self.host,port=self.port,user=self.user,password=self.password,database=self.database)

    # 增删改
    def Execute(self,sql):
        # 1、创建数据库的连接
        databases=self.getconnect()
        # 2、创建执行sql的对象
        cursor=databases.cursor()
        # 3、执行sql命令
        cursor.execute(sql)
        databases.commit()
        # 4、关闭连接
        cursor.close()
        databases.close()
        print('数据更改成功！')
    def Select(self,sql):
        databases=self.getconnect()
        cursor=databases.cursor()
        cursor.execute(sql)
        res=cursor.fetchall()
        cursor.close()
        databases.close()
        print('查询完毕！')
        return res
if __name__ == '__main__':
    demo=SqlUtil('localhost',3306,'root','15358810yang','demo')
