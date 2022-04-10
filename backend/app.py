from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # 禁止中文转义


@app.route("/user/login", methods=["POST"])
def user_login():
    """
    用户登录
    :return:
    """
    data = request.get_json()
    userName = data.get("userName")
    password = data.get("password")
    if userName == "admin" and password == "123456":
        return jsonify({
            "code": 0,
            "data": {
                "token": "666666"
            }
        })
    else:
        return jsonify({
            "code": 99999999,
            "msg": "用户名或密码错误"
        })


@app.route("/user/info", methods=["GET", "POST"])
def user_info():
    """
    获取当前用户信息
    :return:
    """
    token = request.headers.get("token")
    if token == "666666":
        return jsonify({
            "code": 0,
            "data": {
                "id": "1",
                "userName": "admin",
                "realName": "张三",
                "userType": 1
            }
        })
    return jsonify({
        "code": 99990403,
        "msg": "token不存在或已过期"
    })


@app.route("/")
def hello_world():
    return "hello world"


@app.route("api/test", methods=["POST", "GET"])
def get_name():
    # print(request.form)
    # print(request.data)
    print(request.get_json())
    if request.method == 'POST':
        return "is POST"
    else:
        return "is GET"


if __name__ == '__main__':
    app.run(host="127.0.0.1", port="5000", debug=True)

