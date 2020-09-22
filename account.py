# 导入Flask类
from flask import Flask
from flask import render_template
from flask import request
from flask_restful import Api
from flask_restful import Resource
from flask_restful import reqparse

# 实例化，可视为固定格式
app = Flask(__name__)

# 实例化一个api用于配置路由
api = Api(app)

# 实例化一个参数解析类，用于获取get和post提交的参数
parser = reqparse.RequestParser()

# 注册q参数parser才能解析get和post中的q参数。这种注册才能解析的要求是否有点孤儿
parser.add_argument('username', type=str, help='Rate to charge for this resource')
parser.add_argument('password', type=str, help='Rate to charge for this resource')


# 添加Account类（是类而不是和Flask一样直接是方法）
class Account(Resource):
    # get提交时的处理方法
    def get(self):
        result = {}
        args = parser.parse_args()
        username = args["username"]
        password = args["password"]

        if username == 'jingyu':
            # 账号密码正确
            if password == '123456':
                result["success"] = True
                result["code"] = 1000
                result["msg"] = 'login success'
                return result
            else:
                result["success"] = False
                result["code"] = 1001
                result["msg"] = 'password error'
                return result

        result["success"] = False
        result["code"] = 1001
        result["msg"] = 'account not exist'
        return result

    # post提交时的处理方法
    def post(self):
        result = {}
        # 此种方法即可解析通过普通post提交也可解析json格式提交
        args = parser.parse_args()
        result["method"] = "post"
        result["q"] = args["q"]
        return result

# 配置路由
api.add_resource(Account, '/account')

if __name__ == '__main__':
    # app.run(host, port, debug, options)
    # 默认值：host="127.0.0.1", port=5000, debug=False
    app.run(host="127.0.0.1", port=8084)
