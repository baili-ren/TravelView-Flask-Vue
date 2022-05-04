from flask import Flask, request,jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from exts import db
from routes import home_bp, chinaMap_bp
import config
import web_sql

app = Flask(__name__)
app.config.from_object(config)
CORS(app, resources=r'/*')
db.init_app(app)
migrate = Migrate(app, db)
app.config['JSON_AS_ASCII'] = False



# 路由
app.register_blueprint(home_bp)
app.register_blueprint(chinaMap_bp)



@app.route('/api/test')
def test():
    return "测试接口"

# 接口 --- 查询各省的热度与景点数
@app.route('/api/province/info', methods=['POST', 'GET'])
def get_province_info():
    if request.method == "GET":
        data = web_sql.province_sight_count()
        response = []
        for i in data:
            response.append({"provinceName":i[0],"count":int(i[2]),"heat":int(i[1])})

        result = {
            "msg": "各省景点数与热度",
            "data": response
        }
        return jsonify(result)
    else:
        return "/api/province/info"


# 接口 --- 查询各省的5A景区
@app.route('/api/province/5a', methods=['POST', 'GET'])
def get_province_5A():
    if request.method == "GET":
        data = web_sql.province_sight_5a()
        response = []

        for i in data:
            response.append({"provinceName":i[0],
                             "sightName":i[1],
                             "heat":i[2],
                             "intro":i[3],
                             "point":str(i[4]).split(','),
                             "address":i[5],
                             "saleCount":i[6],
                             "price":float(i[7]),
                             "star":i[8],
                             "score":i[9],
                             "commentCount":i[10]
                             })

        result = {
            "msg": "各省5a景点",
            "data": response
        }
        return jsonify(result)
    else:
        try:
            province = request.json['province']
        except KeyError:
            province = ''
        try:
            sightName = request.json['sightName']
        except KeyError:
            sightName = ''
        try:
            star = request.json['star']
        except KeyError:
            star = '5A'
        data = web_sql.province_sight_5a(province=province,sightName=sightName,star=star)
        print(province,sightName,star)
        response = []

        for i in data:
            response.append({"provinceName": i[0],
                             "sightName": i[1],
                             "heat": i[2],
                             "intro": i[3],
                             "point": str(i[4]).split(','),
                             "address": i[5],
                             "saleCount": i[6],
                             "price": float(i[7]),
                             "star": i[8],
                             "score": i[9],
                             "commentCount": i[10]
                             })

        result = {
            "msg": "各省5a景点",
            "data": response
        }
        return jsonify(result)



# 接口 --- 查询各省的推荐景区
@app.route('/api/province/recommend', methods=['POST', 'GET'])
def get_province_recommend():
    if request.method == "GET":
        data = web_sql.province_sight_recommend()
        response = []
        response_data = {}

        for i in data:
            try:
                response_data[i[0]].append(i[1])
            except Exception:
                response_data[i[0]] = [i[1]]

        for province_name in response_data.keys():
            j = []
            for sight_name in response_data[province_name]:
                j.append(sight_name)
            response.append({"provinceName": province_name, "sightName": j})

        result = {
            "msg": "各省推荐景点",
            "data": response
        }
        return jsonify(result)
    else:
        try:
            province = request.json['province']
        except KeyError:
            province = ''
        data = web_sql.province_sight_recommend(province=province)
        response = []
        response_data = {}

        for i in data:
            try:
                response_data[i[0]].append(i[1])
            except Exception:
                response_data[i[0]] = [i[1]]

        for province_name in response_data.keys():
            j = []
            for sight_name in response_data[province_name]:
                j.append(sight_name)
            response.append({"provinceName": province_name, "sightName": j})

        result = {
            "msg": "各省推荐景点",
            "data": response
        }
        return jsonify(result)


# 接口 --- 查询热门景点的经纬度
@app.route('/api/sight/position', methods=['POST', 'GET'])
def get_sight_position():
    if request.method == "GET":
        data = web_sql.sight_geo()
        response = []

        for i in data:
            response.append({"sightName":i[0],"geo":str(i[1]).split(',')})

        result = {
            "msg": "景点定位",
            "data": response
        }
        return jsonify(result)

    elif request.method == "POST":
        pass

    else:
        return "/api/sight/position"


# 接口 --- 查询热门景点的热度
# post请求提交参数查询
@app.route('/api/sight/heat', methods=['POST', 'GET'])
def get_sight_heat():
    if request.method == "GET":
        data = web_sql.sight_heat()
        response = []

        for i in data:
            response_data = {}
            response_data['name'] = i[0]
            response_data['value'] = round(i[1],2)
            response.append(response_data)

        result = {
            "msg": "热门景点热度",
            "data": response
        }
        return jsonify(result)

    elif request.method == "POST":
        try:
            province = request.json['province']
        except KeyError:
            province = ''
        try:
            sightName = request.json['sightName']
        except KeyError:
            sightName = ''
        data = web_sql.sight_heat(province=request.json['province'],sightName=sightName)
        response = []

        for i in data:
            response_data = {}
            response_data['name'] = i[0]
            response_data['value'] = round(i[1], 2)
            response.append(response_data)

        result = {
            "msg": "热门景点热度",
            "data": response
        }
        return jsonify(result)

    else:
        return "/api/sight/position"

# 接口 --- 查询热门景点的位置与热度
# post请求提交参数查询
@app.route('/api/sight/heatPosition', methods=['POST', 'GET'])
def get_sight_heatPosition():
    if request.method == "GET":
        data = web_sql.sight_heat()
        response = []

        for i in data:
            response_data = {}
            response_data['lat'] = str(i[2]).split(',')[1]
            response_data['count'] = round(i[1],2)
            response_data['lng'] = str(i[2]).split(',')[0]
            response.append(response_data)

        result = {
            "msg": "热度位置",
            "data": response
        }
        return jsonify(result)

    elif request.method == "POST":
        try:
            province = request.json['province']
        except KeyError:
            province = ''
        try:
            sightName = request.json['sightName']
        except KeyError:
            sightName = ''
        data = web_sql.sight_heat(province=request.json['province'], sightName=sightName)

        response = []

        for i in data:
            response_data = {}
            response_data['lat'] = str(i[2]).split(',')[1]
            response_data['count'] = round(i[1], 2)
            response_data['lng'] = str(i[2]).split(',')[0]
            response.append(response_data)

        result = {
            "msg": "热度位置",
            "data": response
        }
        return jsonify(result)

    else:
        return "/api/sight/position"


# 接口 --- 查询各省的4A5A景区数量
@app.route('/api/province/4a5aCount', methods=['POST', 'GET'])
def get_province_4a5aCount():
    if request.method == "GET":
        data = web_sql.province_4a5a_count()
        response = {}

        for i in data:
            response[i[0]] = i[1]

        result = {
            "msg": "各省4a5a景点数量",
            "data": response
        }
        return jsonify(result)
    else:
        return "/api/province/4a5aCount"


# 接口 --- 查询评分与热度的关系
@app.route('/api/sight/scoreHeat', methods=['POST', 'GET'])
def get_sight_scoreHeat():
    if request.method == "GET":
        data = web_sql.heat_score()
        response = []

        for i in data:
            response.append([i[2],i[1]])

        result = {
            "msg": "景点评分与热度关系",
            "data": response
        }
        return jsonify(result)
    else:
        return "/api/sight/scoreHeat"

# 接口 --- 查询评分与价格关系
@app.route('/api/sight/scorePrice', methods=['POST', 'GET'])
def get_sight_score_price():
    if request.method == "GET":
        data = web_sql.price_score()
        response = []

        for i in data:
            response.append([i[2],float(i[1])])
        result = {
            "msg": "景点评分与价格关系",
            "data": response
        }
        return jsonify(result)
    else:
        return "/api/sight/scorePrice"



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)



