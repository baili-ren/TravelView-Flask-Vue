from flask import Flask, request
from flask_migrate import Migrate
from flask_cors import CORS
from exts import db
from models import Test_tb, ProvinceScenic_tb, Scenic5A_tb
from routes import home_bp, chinaMap_bp
import json
import config

app = Flask(__name__)
app.config.from_object(config)
CORS(app, resources=r'/*')
db.init_app(app)
migrate = Migrate(app, db)


# 路由
app.register_blueprint(home_bp)
app.register_blueprint(chinaMap_bp)


@app.route('/')
def hello_world():
    # test01 = Test_tb(username="admin01", password="111")
    # test02 = Test_tb(username="admin03", password="111")
    # db.session.add(test01)
    # db.session.add(test02)
    # db.session.commit()

    # ProvinceScenic_tb.query.filter_by().delete()
    # db.session.commit()

    print(1234)
    data1 = Test_tb.query.all()
    data_serialize = []
    for i in data1:
        data_serialize.append(i.test_schema())

    result = {
        "msg": "testData",
        "data": data_serialize,
    }
    return result


@app.route('/api/test')
def test():
    return "测试接口"

# 接口 --- 查询某省的5A景区
@app.route('/api/province/5a', methods=['POST', 'GET'])
def get_province_5A():
    if request.method == "POST":
        params = request.get_data()
        params = json.loads(params.decode("utf-8"))
        province = params["province"]

        data = Scenic5A_tb.query.filter_by(provinceName=str(province)).all()
        data_serialize = []
        for i in data:
            data_serialize.append(i.schema())
        result = {
            "msg": province + "5A景区",
            "data": data_serialize
        }
        return result
    else:
        return "/api/province/5a"



if __name__ == '__main__':
    app.run(host="127.0.0.1", port="5000", debug=True)

