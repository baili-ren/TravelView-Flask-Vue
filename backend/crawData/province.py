# -*- codeing = utf-8 -*-
# @Author: zhangfan
# @File: province.py
# @Software: PyCharm

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
from models import ProvinceScenic_tb, Scenic5A_tb, ScenicType_tb
from crawData import proxList
import requests
import parsel
import re
import config

main = Flask(__name__)
main.config.from_object(config)
db = SQLAlchemy(main)
db.init_app(main)



# 各省份推荐的列表
def crawProviceData():
    # 各省的推荐景点
    for item in provinceList:
        char = "5A"
        url_province = "https://piao.qunar.com/ticket/list.htm?keyword="+quote(item)+"&region=&from=mps_search_suggest&page=1"
        # 各省推荐的景区
        response = requests.get(url_province, headers=headers)
        html_data = response.text
        selector = parsel.Selector(html_data)
        print(item,"行政区")
        scenicNameList = selector.css("#search-list > div > div > div.sight_item_about > h3 > a::text").getall()
        scenicTypeList= selector.css("#subject-list > dd> a > span::text").getall()
        print("scenicTypeList=========",scenicTypeList)
        j = 1
        while j < len(scenicTypeList):
            num = ''.join(re.findall(r"\d+\.?\d*",scenicTypeList[j]))
            scenicType = ''.join(re.findall(re.compile(u'[\u4e00-\u9fa5]'), scenicTypeList[j]))
            data = ScenicType_tb(provinceName=item, ScenicType=scenicType, ScenicNum=num)
            j = j + 1
            print(scenicType,num,"scenicType========num==============")
            db.session.add(data)
        db.session.commit()


        # 将数据保存到mysql
        print("推荐的景区", scenicNameList, len(scenicNameList))
        i = 0
        listLen = len(scenicNameList)
        while i < listLen:
            data = ProvinceScenic_tb(provinceName = item, ScenicName=scenicNameList[i])
            i = i + 1
            print(data, data.schema(),"data---------------")
            db.session.add(data)
        db.session.commit()
    return "获取各省推荐的景点"


def crawProvince5A():
    for item in provinceList:
        char = "5A"
        page = 1
        scenic5ANameList = []
        while page < 2:
            url_province_5A = "https://piao.qunar.com/ticket/list.htm?keyword="+quote(item + char)+"&region=&from=mps_search_suggest&page="+str(page)
            page = page + 1
            # 各省的5A景区
            prox = proxList
            # ip 代理
            response = requests.get(url_province_5A,headers=headers, proxies=prox, timeout=10)
            print(response,"response")
            html_data = response.text
            selector = parsel.Selector(html_data)
            scenic5ANameList = scenic5ANameList + selector.css("#search-list > div > div > div.sight_item_about > h3 > a::text").getall()

        print(item, "行政区")
        print(scenic5ANameList, len(scenic5ANameList), "5A景区")
        # 将数据存到mysql
        i = 0
        while i < len(scenic5ANameList):
            data = Scenic5A_tb(provinceName=item, Scenic5AName=scenic5ANameList[i])
            i = i+1
        #     db.session.add(data)
        # db.session.commit()


def thread():
    # from flask import app
    with main.app_context():
        data1 = ProvinceScenic_tb.query.all()
        data_serialize = []
        for i in data1:
            data_serialize.append(i.schema())
        print(data_serialize, "999")
        result = {
            "msg": "testData",
            "data": data_serialize,
        }
        return result

def main():
    # thread()
    # crawProvince5A()
    crawProviceData()

if __name__ == '__main__':
    # 获取全国省份列表
    provinceList = ["安徽","北京","重庆","福建","甘肃","广东","广西","贵州","海南","河北","河南","黑龙江","湖北","湖南","吉林","江苏","江西","辽宁","内蒙古","宁夏","青海","山东","山西","陕西","上海","四川","天津","西藏","新疆","香港","云南","澳门","浙江"]
    headers={
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'cookie': 'QN1=dXrghVzaM0cN+wYpRryRAg==; QN269=9B0D2CC075F511E9BCA9FA163ED025F3; _i=ueHd8xMxBTVXqvCA4qR470Um5eyX; QunarGlobal=10.86.213.150_21340582_16ab448be93_7a80|1557803849001; QN99=647; fid=eda14267-76af-406d-975d-9e098c9d50f4; __utma=183398822.428737805.1557803850.1557803850.1557803850.1; __utmz=183398822.1557803850.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr=%E5%A5%BD123%E6%97%85%E6%B8%B8; _jzqa=1.1924495795568354000.1557803852.1557803852.1557803852.1; _jzqx=1.1557803852.1557803852.1.jzqsr=hotel%2Equnar%2Ecom|jzqct=/.-; QN71="NTguMjQzLjI1NC4xMjk65a6J5b69OjE="; QN57=15578038546700.26539516250028505; QN67=1211; cto_lwid=06e141f7-870f-42ca-9519-312c3587bed8; QN63=%E7%83%AD%E9%97%A8%E6%99%AF%E7%82%B9%7C%E5%AE%89%E5%BE%BD; csrfToken=ZrtgmFh4YnLvKzqP8dCzzti2JoLh7sFz; _vi=3di8PYGZ-R9GtBBMOJN2tlBVR_KX-2jyHo6YmCS3JC-NB1B9rZnnrT7ZlQIEIdYWcInEmtNp0xdr9Aaf4mU9WCoN7q_-8QEnQ3m2goXxwFZpqYH8gGaupHTLFP-ak8JMAES3K_yVSwvsNpRb_qYHXgc4xajzIvF93Hnj_YkbVQDN; Hm_lvt_15577700f8ecddb1a927813c81166ade=1557803855,1558319263; QN300=auto_4e0d874a; QN205=auto_4e0d874a; QN277=auto_4e0d874a; QN267=79056878cd9f7ec1; QN58=1558319262033%7C1558319518464%7C2; Hm_lpvt_15577700f8ecddb1a927813c81166ade=1558319519; JSESSIONID=A509706026389E421E058210F3BEF192; Request-Node=f6769d42991e67d1c5a98893de33d1f3; QN271=06f7c456-ac81-4bdb-b833-ddfbc81ab633',
        'Host': 'piao.qunar.com',
        'Referer': 'http://piao.qunar.com/ticket/list.htm?keyword=%E7%83%AD%E9%97%'
                   'A8%E6%99%AF%E7%82%B9&region=&from=mpl_search_suggest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    main()
