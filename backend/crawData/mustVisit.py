# -*- codeing = utf-8 -*-
# @Author: zhangfan
# @File: mustVisit.py
# @Software: PyCharm


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import HotCityPlace_tb
import requests
import parsel
import config


main = Flask(__name__)
main.config.from_object(config)
db = SQLAlchemy(main)

# 热门城市-必游景点
def crawHotCity():
    url = "https://piao.qunar.com/"
    response = requests.get(url)
    html_data = response.text
    selector = parsel.Selector(html_data)
    # 热门城市的名字
    hotCityNameList = selector.css('body > div.piao_wrap > div.mp-main > div.mp-header > div.mp-header-bottom > div.mp-sidebar > div:nth-child(1) > ul > li > a::text').getall()
    print(hotCityNameList,"hotCityNameList")

    for item in hotCityNameList:
        print('-----------------------', item, '----------------------')
        detail_url = "https://piao.qunar.com/index.htm?region="+item+"&from=mpshouye_city"
        response = requests.get(detail_url)
        html_data = response.text
        selector = parsel.Selector(html_data)

        # 热门城市下的热门景点名称
        placeNameList = selector.css("body > div.piao_wrap > div.mp-main > div:nth-child(5) > div.mp-section-content > ul:nth-child(1) > li > a > div.mp-section-content-info > h4::text").getall()
        print(placeNameList, "placeNameList01")
        if placeNameList == []:
            placeNameList = selector.css("body > div.piao_wrap > div.mp-main > div:nth-child(4) > div.mp-section-content > ul:nth-child(1) > li > a > div.mp-section-content-info > h4::text").getall()
            print(placeNameList,"placeNameList02")

        # 将数据保存到mysql
        i = 0
        placeNameListLen = len(placeNameList)
        while i < placeNameListLen:
            data = HotCityPlace_tb(ctiyName=item, placeName=placeNameList[i])
            i = i + 1
            print(data, data.schema(), "data--------------")
            db.session.add(data)
        db.session.commit()
    return "获取热门城市"


def main():
    crawHotCity()


if __name__ == '__main__':
    main()


