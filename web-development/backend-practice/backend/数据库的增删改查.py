import pymysql
#连接MySQL数据库并建立表
def Connect():
    #连接数据库
    conn=pymysql.connect(
        host='localhost',
        user='root',
        password='15358810yang',
        database='demo',
        charset='utf8mb4',
        port=3306
    )
    #确立游标对象执行下来的SQL指令
    cursor=conn.cursor()
    #如果表存在就删除，以防重复建表导致报错
    sql1='''drop table if exists hero'''
    cursor.execute(sql1)
    #建立王者荣耀英雄信息表
    sql2='''create table hero(
         id int primary key auto_increment comment'编号',
         sname varchar(10) not null comment'名字',
         sex enum('男','女') comment'性别',
         age int not null comment'年龄',
         height int not null comment'身高'
          )
        '''
    cursor.execute(sql2)
    print('英雄表建立成功！')
#增添数据模块
def Insert():
    #连接数据库
    conn=pymysql.connect(
        host='localhost',
        user='root',
        password='15358810yang',
        database='demo',
        charset='utf8mb4',
        port=3306
    )
    #确立游标对象执行接下来的SQL指令
    cursor=conn.cursor()
    #插入第一条英雄信息
    sql1='''insert into hero values(default,'小乔','女',16,165)'''
    cursor.execute(sql1)
    #将列表内的信息插入英雄表(注:0代表无指定ID，ID跟随原设定表的插入顺序自然增长；
    sqarm=[
           (0,'大乔','女',18,170),
           (0,'孙尚香','女',18,180),
           (0,'成吉思汗','男',20,185),
           (0,'耀','男',19,180),
           (0,'程咬金','男',35,175)
    ]
    #注：%s为占位符，数量必须与表中列个数相等(%s不代表插入字符串s，而是一个'空位',数据会一一对应占据空位)
    sql2='''insert into hero values(%s,%s,%s,%s,%s);
    '''
    cursor.executemany(sql2,sqarm)
    #用于提交事务（将更改的数据提交到数据库永久保存，若是省去这行代码，一但断开数据库连接，数据库的数据会恢复原样）
    conn.commit()
    cursor.close()
    conn.close()
#删除数据模块
def Delete():
    #连接数据库
     conn=pymysql.connect(
        host='localhost',
        user='root',
        password='15358810y.ang',
        database='demo',
        charset='utf8mb4',
        port=3306
     )
     cursor=conn.cursor()
     #删除id=3的信息
     sql='''delete from hero where id=3'''
     cursor.execute(sql)
     #提交修改数据
     conn.commit()
     #先关闭游标对象，再关闭数据库连接，释放连接数据库和游标占用的资源
     cursor.close()
     conn.close()
     print('OK!')
#修改数据模块
def Update():
    #连接数据库
    conn=pymysql.connect(
        host='localhost',
        user='root',
        password='15358810yang',
        database='demo',
        charset='utf8mb4',
        port=3306
    )
    cursor=conn.cursor()
    #修改sname=程咬金的数据
    sql='''update hero set height=180,age=50 where sname='程咬金';
    '''
    cursor.execute(sql)
    print('信息更改完毕！')
    #提交数据
    conn.commit()
    #释放资源
    cursor.close()
    conn.close()
#查询数据模块
def Select():
    #连接数据库
    conn=pymysql.connect(
        host='localhost',
        user='root',
        password='15358810yang',
        database='demo',
        charset='utf8mb4',
        port=3306
    )
    cursor=conn.cursor()
    #查询所有英雄表的信息
    sql='''select * from hero'''
    cursor.execute(sql)
    #fetch 获取
    res=cursor.fetchone()#获取一条数据
    res_all=cursor.fetchall()#获取所有数据
    res_many=cursor.fetchmany()#获取指定数量的数据 不指定时 默认数量值为1
    print(res)
    #释放资源
    cursor.close()
    conn.close()

#调用模块的函数
if __name__ == '__main__':
    Connect()
    Insert()
    Delete()
    Update()
    Select()