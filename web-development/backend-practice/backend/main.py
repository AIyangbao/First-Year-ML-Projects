from flask import Flask
from flask import request
from SqlUtils import SqlUtil
import json,os,time,random

app = Flask(__name__)

@app.route('/test')
def test():
    return 'flask is ok'

#注册接口
@app.route('/reg',methods=['POST'])
def reg():
    username = request.form.get('username')
    password = request.form.get('password')
    print(username,password)
    db = SqlUtil('localhost',3306,'root','15358810yang','testdb')
    #先查询用户名是否已经存在
    sql =f'''select * from users where loginName='{username}';'''
    res = db.Select(sql)
    if len(res) > 0:
        #存在则注册失败
        return {'code':400,'msg':'注册失败，用户名已经存在'}
    # 不存在则将用户传递过来的数据写入到表格中储存起来,注册成功
    sql =f''' insert into users values(default,{username},'{password}',now());'''
    db.Execute(sql)
    return {'code':200,'msg':'注册成功'}

#登录接口
@app.route('/login',methods=['POST'])
def login():
    user = request.form.get('username')
    pwd = request.form.get('password')
    db = SqlUtil('localhost',3306,'root','15358810yang','testdb')
    sql =f"""select * from users where loginName='{user}' and loginPwd='{pwd}'"""
    res = db.Select(sql)
    if len(res) > 0:
        return{'code':200,'msg':'登陆成功'}
    return {'code':400,'msg':'登录失败'}

#更改密码接口
@app.route('/forget',methods=['POST'])
def forget():
    user = request.form.get('username')
    pwd = request.form.get('password')
    db = SqlUtil('localhost',3306,'root','15358810yang','testdb')
    sql = f""" select * from users where loginName='{user}';'"""
    res = db.Select(sql)
    if len(res) ==0:
        return {'code':400,'msg':'修改失败'}
    sql =f""" update users set loginPwd='{pwd}' where loginName='{user}';"""
    db.Execute(sql)
    return {'code':200,'msg':'修改成功'}

#获取导航列表接口
def nav_list():
    sql ="""select * from navigation;"""
    db = SqlUtil('localhost',3306,'root','15358810yang','testdb')
    res = db.Select(sql)
    result = []
    for i in res:
        temp = {
            'name':i[1],
            'url':i[2]
        }
        result.append(temp)
    return json.dumps(result)

#添加导航接口
@app.route('/nav/add',methods=['POST'])
def nav_add():
    title = request.form.get('title')
    url = request.form.get('url')
    db = SqlUtil('localhost',3306,'root','15358810yang','testdb')
    sql =f""" select * from navigation where dName='{title}' """
    res = db.Select(sql)
    if len(res) > 0:
        return{'code':400,'msg':'添加失败，导航已存在'}
    
    sql = f""" insert into navigation values(default,'{title}','{url}')"""
    db.Execute(sql)
    return {'code':200,'msg':'添加成功'}

#删除导航接口
@app.route('/nav/del',methods=['POST'])
def nav_del():
    id = request.form.get('id')
    db = SqlUtil('localhost',3306,'root','15358810yang','testdb')
    sql = f''' select * from navigation where id ={id}'''
    res = db.Select(sql)
    if len(res) ==0 :
        return{'code':400,'msg':'删除失败，没有此导航'}
    
    sql = f''' delete from navigation where id={id}'''
    db.Execute(sql)
    return {'code':200,'msg':'删除成功'}

#获取新闻列表接口
@app.route('/news/list')
def news_list():
    sql =''' select * from news; '''
    db = SqlUtil('localhost',3306,'root','15358810yang','testdb')
    res = db.Select(sql)
    result = []
    for i in res:
        temp = {
            'id':i[0],
            'title':i[1],
            'img':i[2],
            'content':i[3]
        }
        result.append(temp)
    return json.dumps(result)

#上传图片接口
@app.route('/news/save/pic',methods=['POST'])
def news_save_pic():
    img = request.files.get('img')
    print(img)
    suffix =img.filename.split('.')[-1]
    if suffix not in ['png','jpg']:
        return {'code':400,'msg':'上传失败'}
    
    dir = 'project/static/news'
    if not os.path.exists(dir):
        os.makedirs(dir)#创建多层目录
    #图片 文件名重复的情况
    img.save(f'{dir}/{int(time.time()*1000)}{random.randint(999,99999)}.png')
    return {'code':200,'msg':'上传成功'}

#添加新闻接口
@app.route('/news/add',methods=['POST'])
def news_add():
    title = request.form.get('title')
    img = request.form.get('img')
    content =request.form.get('content')
    navid = request.form.get('navid')
    db = SqlUtil('localhost',3306,'root','15358810yang','testdb')
    sql =f''' select * from news where title='{title}' '''
    res = db.Select(sql)
    if len(res) > 0:
        return {'code':400,'msg':'添加失败'}
    sql = f""" insert into news values(default,'{title}','{img}','{content}',now(),'{navid}')"""
    db.Execute(sql)
    return {'code':200,'msg':'删除成功'}

#删除新闻信息接口
@app.route('/news/del',methods=['POST'])
def news_del():
    id = request.form.get('id')
    db = SqlUtil('localhost',3306,'root','15358810yang','testdb')
    sql = f''' select * from news where id={id}'''
    res = db.Select(sql)
    if len(res) == 0:
        return {'code':400,'msg':'删除失败'}
    sql = f''' delete from news where id={id} '''
    db.Execute(sql)
    return {'code':200,'msg':'删除成功'}

#修改新闻信息接口
@app.route('/news/modify',methods=['POST'])
def news_modify():
    id = request.form.get('id')
    title = request.form.get('title')
    img = request.form.get('img')
    content = request.form.get('content')
    navid = request.form.get('navid')
    db = SqlUtil('localhost',3306,'root','15358810yang','testdb')
    sql = f''' select * from news where id={id} '''
    res = db.Select(sql)
    if len(res) == 0:
        return{'code':200,'msg':'修改失败，未有此新闻'}
    sql =f''' update news set title='{title}',img='{img}',content='{content}',
                              navId={navid} where id={id};
                              '''
    db.Execute(sql)
    return {'code':200,'msg':'登陆成功'}

if __name__ == '__main__':
    db = SqlUtil('localhost',3306,'root','15358810yang','testdb')
    sql = ''' insert into  navigation values(default,'公司首页','http://127.0.0.1:5005/a.html'),
                                         (default,'公司动态','http://127.0.0.1:5005/b.html'); '''
    db.Execute(sql)
    sql = """
         insert into news values(default,'新闻1','http://127.0.0.1:5005/static/news/a.jpg','测试信息1',now(),1),
                                 (default,'新闻2','http://127.0.0.1:5005/static/news/b.jpg','测试信息2',now(),2);
     """
    db.Execute(sql)
    for i in range(10):
         print(f'{int(time.time() * 1000)}{random.randint(999,99999)}')  # 时间戳  1970年1月1日0时0分0秒到现在的总秒数
         time.sleep(1)
    print('-----------------users-----------------')
    print(db.Select('''select * from users;'''))
    print('-----------------navigation-----------------')
    print(db.Select('''select * from navigation;'''))
    print('-----------------news-----------------')
    print(db.Select('''select * from news;'''))
    app.run(port=5005)



