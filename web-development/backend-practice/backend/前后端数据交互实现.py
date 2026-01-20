from flask import Flask
from flask import request
from flask_cors import CORS
import json
app = Flask(__name__)
CORS(app,resources='/*')#/*代表可以把数据返回到任意位置

@app.route('/login',methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    print(username,password)
    if username == 'admin' and password == '123456':
        return json.dumps({'code':200,'msg':'登陆成功'},ensure_ascii=False)#ensure_ascii正常显示中文
    return json.dumps({'code':400,'msg':'登录失败'},ensure_ascii=False)
if __name__ == "__main__":
    app.run(port=5005)
                      
    