# -*- codeing = utf-8 -*-
# @Author: zhangfan
# @File: mustVisit.py
# @Software: PyCharm
import requests
import parsel
import pymysql


# 热门城市-必游景点
def getHotCity():
    url = "https://piao.qunar.com/"
    response = requests.get(url)
    html_data = response.text
    selector = parsel.Selector(html_data)
    hotCityNameList = selector.css('body > div.piao_wrap > div.mp-main > div.mp-header > div.mp-header-bottom > div.mp-sidebar > div:nth-child(1) > ul > li > a::text').getall()
    print(hotCityNameList)
    # for item in hotCityNameList:
    #     detail_url = "https://piao.qunar.com/index.htm?region="+item+"&from=mpshouye_city"
    #     response = requests.get(detail_url)
    #     print(response.status_code, item)
    #     html_data = response.text
    #     selector = parsel.Selector(html_data)
    #     placeNameList = selector.css("body > div.piao_wrap > div.mp-main > div:nth-child(3) > div.mp-section-content > ul > li > a > div.mp-section-content-info > h4::text").getall()
    #     print(placeNameList)
    #     placeIntroduceList = selector.css("body > div.piao_wrap > div.mp-main > div:nth-child(3) > div.mp-section-content > ul > li > a > div.mp-section-content-info > p::text").getall()
    #     print(placeIntroduceList)

    return "获取热门城市"

class down_mysql:
    def __init__(self, city_name, place_name, palce_introdce):
        self.city_name = city_name
        self.place_name = place_name
        self.palce_introdce = palce_introdce
        self.connect = pymysql.connect(
            host='127.0.0.1',
            db='travel_flask',
            port=3306,
            user='root',
            passwd='1234CDcd',
            charset='utf8',
            use_unicode=False
        )
        self.cursor = self.connect.cursor()

    # 保存数据到MySQL中
    def save_mysql(self):
        sql = "insert into must_visit_place(city_name, place_name, place_introduce) VALUES (%s,%s,%s)"
        try:
            self.cursor.execute(sql, (
            self.city_name, self.place_name, self.palce_introdce, ))
            self.connect.commit()
            print('数据插入成功')
        except Exception as e:
            print('数据插入错误',e)

def mysql(city_name, place_name, palce_introdce):
    # 新建类，将数据保存在MySQL中
    down = down_mysql(city_name, place_name, palce_introdce)
    down.save_mysql()


def startCraw():
    getHotCity()
    mysql("北京", "故宫", "故宫简介")
    return '爬取数据'


if __name__ == '__main__':
    startCraw()

