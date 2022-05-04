import requests
import reptile_sql
import time
import random

class QunaerReptile:
    def __init__(self):
        self.session = requests.session()
        self.baseurl = 'https://piao.qunar.com'
        self.city_list = ['北京', '天津', '山西', '河北', '山东', '河南', '广东', '浙江', '宁夏', '江苏', '湖南', '吉林', '福建', '甘肃', '陕西', '辽宁', '江西', '黑龙江', '安徽', '湖北', '青海', '新疆', '贵州', '四川', '上海', '广西', '西藏', '云南', '内蒙古', '海南', '重庆', '台湾', '香港', '澳门']
        self.max_page = 4 # 最大爬取页数，每页15条景点
        self.UserAgent = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A', 'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.13+ (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10', 'Mozilla/5.0 (iPad; CPU OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko ) Version/5.1 Mobile/9B176 Safari/7534.48.3', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; de-at) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; da-dk) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; tr-TR) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; ko-KR) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; fr-FR) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; cs-CZ) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; ja-JP) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27', 'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; zh-cn) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27', 'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; ja-jp) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; ja-jp) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; zh-cn) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; sv-se) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; ko-kr) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; ja-jp) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; it-it) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; fr-fr) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; es-es) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-us) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-gb) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; de-de) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; sv-SE) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; ja-JP) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; de-DE) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; hu-HU) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; de-DE) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; ru-RU) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; ja-JP) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it-IT) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_7; en-us) AppleWebKit/534.16+ (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; fr-ch) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; de-de) AppleWebKit/534.15+ (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; ar) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4', 'Mozilla/5.0 (Android 2.2; Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-HK) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; tr-TR) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; nb-NO) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5', 'Mozilla/5.0 (Windows; U; Windows NT 6.0; fr-FR) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-TW) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; ru-RU) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; zh-cn) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5']



    def load_headers(self, headers):
        headers = [i.split(': ') for i in headers.split('\n') if len(i.strip()) > 0]
        headers = dict([[i.strip() for i in i] for i in headers])
        headers['User-Agent'] = random.choice(self.UserAgent) # 使用随机请求头反反爬
        return headers


    def get_cookie(self):
        '''
        获取初始cookie
        :return:
        '''
        url = f'{self.baseurl}/'
        headers = '''
        Host: piao.qunar.com
        Cache-Control: max-age=0
        Sec-Ch-Ua: " Not A;Brand";v="99", "Chromium";v="100", "Microsoft Edge";v="100"
        Sec-Ch-Ua-Mobile: ?0
        Sec-Ch-Ua-Platform: "macOS"
        Dnt: 1
        Upgrade-Insecure-Requests: 1
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
        Sec-Fetch-Site: none
        Sec-Fetch-Mode: navigate
        Sec-Fetch-User: ?1
        Sec-Fetch-Dest: document
        Accept-Encoding: gzip, deflate
        Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
        '''
        cookie = self.session.get(url = url,headers=self.load_headers(headers))
        time.sleep(random.randint(5,30)/10) #随机等待，防止触发反爬

    def sight_List(self,province,page):
        '''
        获取各省份的旅游景点数据
        :param province: 省份名
        :return:
        '''
        url = f'{self.baseurl}/ticket/list.json?keyword={province}&region=&from=mps_search_suggest&sku=&page={page}&subject='
        headers = '''
        Host: piao.qunar.com
        Sec-Ch-Ua: " Not A;Brand";v="99", "Chromium";v="100", "Microsoft Edge";v="100"
        Accept: application/json, text/javascript, */*; q=0.01
        Dnt: 1
        X-Requested-With: XMLHttpRequest
        Sec-Ch-Ua-Mobile: ?0
        Sec-Ch-Ua-Platform: "macOS"
        Sec-Fetch-Site: same-origin
        Sec-Fetch-Mode: cors
        Sec-Fetch-Dest: empty
        Referer: https://piao.qunar.com/ticket/list.htm?keyword=%E6%B9%96%E5%8C%97&region=&from=mps_search_suggest&sku=&page=1&subject=
        Accept-Encoding: gzip, deflate
        Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6        
        '''
        data = self.session.get(url = url,headers=self.load_headers(headers)).json()
        return data

    def sight_score(self,sight_id):
        '''
        单个景点的评价数据
        :param sight_id: 景点ID
        :return:
        '''
        url = f'{self.baseurl}/ticket/detailLight/sightCommentList.json?sightId={sight_id}&index=1&page=1&pageSize=10&tagType=0'
        headers = '''
        Host: piao.qunar.com
        Sec-Ch-Ua: " Not A;Brand";v="99", "Chromium";v="100", "Microsoft Edge";v="100"
        Accept: application/json, text/javascript, */*; q=0.01
        Dnt: 1
        X-Requested-With: XMLHttpRequest
        Sec-Ch-Ua-Mobile: ?0
        Sec-Ch-Ua-Platform: "macOS"
        Sec-Fetch-Site: same-origin
        Sec-Fetch-Mode: cors
        Sec-Fetch-Dest: empty
        Referer: https://piao.qunar.com/ticket/detail_5447752.html?st=a3clM0QlRTUlQjklQkYlRTQlQjglOUMlMjZpZCUzRDI5NzQlMjZ0eXBlJTNEMCUyNmlkeCUzRDE2JTI2cXQlM0RyZWdpb24lMjZhcGslM0QyJTI2c2MlM0RXV1clMjZ1ciUzRCVFNiVCNyVCMSVFNSU5QyVCMyUyNmxyJTNEJUU2JUI3JUIxJUU1JTlDJUIzJTI2ZnQlM0QlN0IlN0Q%3D
        Accept-Encoding: gzip, deflate
        Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
        '''
        data = self.session.get(url = url,headers=self.load_headers(headers)).json()
        return data

    def province_sight_list(self,province):
        for i in range(self.max_page):
            data = self.sight_List(province,i+1)
            sight_data = data['data']['sightList']
            for sight in sight_data:
                score = sight['score']
                sightId = sight['sightId']
                try:
                    intro = sight['intro']
                except:
                    intro = '无'
                free = sight['free']
                point = sight['point']
                try:
                    address = sight['address']
                except:
                    address = '无'

                sightName = sight['sightName']
                districts = sight['districts']
                saleCount = sight['saleCount']
                try:
                    qunarPrice = sight['qunarPrice']
                except:
                    qunarPrice = 0
                try:
                    star = sight['star']
                except:
                    star = '无'
                print(score,sightId,intro,free,point,address,sightName,districts,saleCount,qunarPrice,star)
                try:
                    reptile_sql.insert_sight_list((score,sightId,intro,free,point,address,sightName,districts,saleCount,qunarPrice,star,province))
                except:
                    pass

                try:
                    time.sleep(random.randint(8, 30) / 10)
                    sight_comment_data = self.sight_score(sightId) #爬评价数据
                    sight_score = sight_comment_data['data']['score']
                    sight_commentCount = sight_comment_data['data']['commentCount']
                    reptile_sql.insert_sight_score((sightId,sight_score,sight_commentCount))
                except:
                    pass
            if i == 0: #第一次爬该省份时获取该省份的不同类型景点的数量
                subjects_data = data['data']['filter']['subjects']
                for subjects in subjects_data:
                    reptile_sql.insert_province_sight_subjects((province,subjects['name'],subjects['count'],f"{province}{subjects['name']}"))

            time.sleep(random.randint(8,30)/10)

    def run(self):
        for city in self.city_list:
            print(city)
            self.province_sight_list(city)




if __name__ == '__main__':
    reptile = QunaerReptile()
    reptile.get_cookie()
    reptile.run()











