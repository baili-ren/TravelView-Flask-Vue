from flask import Flask, jsonify
from flask_migrate import Migrate
from exts import db
from models import Test_tb
from routes import home_bp, chinaMap_bp
import config

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)
migrate = Migrate(app, db)


# 路由
app.register_blueprint(home_bp)
app.register_blueprint(chinaMap_bp)


@app.route('/')
def hello_world():

    # 写一个测试代码来验证是否连接成功
    engine = db.get_engine()
    with engine.connect() as conn:
        result = conn.execute("select 1")
        print(result.fetchone())

    # test01 = Test_tb(username="admin01", password="111")
    # test02 = Test_tb(username="admin02", password="111")
    # print(test01)
    # db.session.add(test01)
    # db.session.add(test02)
    # db.session.commit()

    data1 = Test_tb.query.first()
    data_serialize = data1.test_schema()
    print(data1, data_serialize,111)
    print(jsonify(data_serialize),222)
    # data2 = data1.schema()
    # print(data2, jsonify(data2),222)
    return data_serialize


if __name__ == '__main__':
    app.run(host="127.0.0.1", port="5000", debug=True)

