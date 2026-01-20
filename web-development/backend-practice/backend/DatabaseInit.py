import pymysql
from SqlUtils import SqlUtil

class DBInit:
    def __init__(self,_dbname):
        self.dbname=_dbname

    #创建数据库
    def createDB(self):
        db =SqlUtil('localhost',3306,'root','15358810yang','sys')
        sql=f'''drop database if exists {self.dbname};'''
        db.Execute(sql)

        sql=f'''create database {self.dbname} charset='utf8mb4';'''
        db.Execute(sql)
        
    #创建数据表
    def createTable(self):
        db = SqlUtil('localhost',3306,'root','15358810yang',f'{self.dbname}')

        sql ='''drop table if exists users;'''
        db.Execute(sql)
        users_sql = '''create table users(
                       id int primary key auto_increment comment'用户编号',
                       loginName varchar(20) comment '登录账号',
                       loginPwd varchar(20) comment'登录密码',
                       cTime datetime comment'创建时间')
                    '''
        db.Execute(users_sql)

        sql='''drop table if exists navigation;'''
        db.Execute(sql)
        navigation_sql='''create table navigation(
                          id int primary key auto_increment comment'导航编号',
                          dName varchar(20) comment'导航名称',
                          dUrl varchar(100) comment'导航地址')
                       '''
        db.Execute(navigation_sql)

        sql='''drop table if exists news;'''
        db.Execute(sql)
        news_sql='''create table news(
                    id int primary key auto_increment comment'新闻编号',
                    title varchar(20) comment'新闻标题',
                    img varchar(100) comment'图片地址',
                    content varchar(200) comment '内容',
                    cTime datetime comment '创建时间',
                    navId int comment '导航编号')      
                 '''
        db.Execute(news_sql)

        sql='''show tables;'''
        res=db.Select(sql)
        print(res)

if __name__ == "__main__":
    obj=DBInit('testdb')
    obj.createDB()
    obj.createTable()
    print('ok')


