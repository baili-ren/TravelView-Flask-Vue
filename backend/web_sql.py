import pymysql
import config


def test_connection():
    try:
        db.ping()
    except:
        db = pymysql.connect(host=config.HOSTNAME, user=config.USERNAME, password=config.PASSWORD,
                             database=config.DATABASE)
    return db


def province_sight_count():
    '''
    获取各省份的景点数量与热度
    :return:
    '''
    sql_v = '''
        SELECT
            sl.province 省份,
            sum( saleCount * score ) 热度,
            t1.count 景点数
        FROM
            sight_list sl
            JOIN ( SELECT province, sum( count ) count FROM province_sight_subjects GROUP BY 1 ) t1 ON t1.province = sl.province 
        GROUP BY 1 
        ORDER BY 2
	'''
    db = test_connection()
    cur = db.cursor()
    cur.execute(sql_v)
    return cur.fetchall()

def province_sight_5a(province='',sightName='',star='5A'):
    '''
    获取各省的5A景点
    :return:
    '''
    if province != '':
        province = f"and province = '{province}'"
    if sightName != '':
        sightName = f"and sightName like '%{sightName}%'"
    if province != '' and sightName != '' and star != '': # 如果提供省份或者景点名称，就不限制5A景点
        star = ""
    else:
        star = f"and star = '{star}'"

    sql_v = f'''
    SELECT
            province 省份,
            sightName 景点名称,
            sl.score 热度,
            intro 简介,
            point 经纬度,
            address 地址,
            saleCount 销售数量,
            qunarPrice 销售价格,
            star 星级,
            ss.score 评分,
            ss.commentCount 评价人数
    FROM
            sight_list sl
            JOIN sight_score ss ON sl.sightId = ss.sightId
    WHERE
            1 = 1
            {province}
            {sightName}
            {star}
	'''
    db = test_connection()
    cur = db.cursor()
    cur.execute(sql_v)
    return cur.fetchall()


def province_sight_recommend(province=''):
    '''
    获取各省的推荐景点
    :return:
    '''
    if province != '':
        province = f"and province = '{province}'"
    sql_v = f'''
    SELECT
        province,
        sightName
    FROM
        sight_list sl
    WHERE
        star != '无'
        {province}
	'''
    db = test_connection()
    cur = db.cursor()
    cur.execute(sql_v)
    return cur.fetchall()


def sight_geo():
    '''
    景点的经纬度信息
    :return:
    '''
    sql_v = '''
    SELECT
        sightName,
        point
    FROM
        sight_list sl
    WHERE
        score >= 4
    ORDER BY score DESC
	'''
    db = test_connection()
    cur = db.cursor()
    cur.execute(sql_v)
    return cur.fetchall()




def sight_heat(province='',sightName=''):
    '''
    景点的热度信息
    :return:
    '''
    if province != '':
        province = f"and province = '{province}'"
    if sightName != '':
        sightName = f"and sightName like '%{sightName}%'"

    sql_v = f'''
    SELECT
        sightName,
        saleCount * score,
        point
    FROM
        sight_list sl
    WHERE
        score >= 4
        AND saleCount > 30
        {province}
        {sightName}
    ORDER BY saleCount * score DESC
	'''

    db = test_connection()
    cur = db.cursor()
    cur.execute(sql_v)
    return cur.fetchall()


def province_4a5a_count():
    '''
    获取各省4A5A景点数量
    :return:
    '''
    sql_v = '''
    SELECT
            province,
            count(sightId)
    FROM
            sight_list sl
    WHERE
            star in ('4A','5A')
    GROUP BY 1
    ORDER BY 2 DESC
	'''
    db = test_connection()
    cur = db.cursor()
    cur.execute(sql_v)
    return cur.fetchall()

def heat_score():
    '''
    获取热度与评分
    :return:
    '''
    sql_v = '''
    SELECT
            sightName,
            sl.score * saleCount 热度,
            ss.score 评分
    FROM
            sight_list sl
            JOIN sight_score ss ON sl.sightId = ss.sightId
    WHERE
            sl.score * saleCount >= 500
            AND sl.saleCount != 0
    ORDER BY 2 DESC
	'''
    db = test_connection()
    cur = db.cursor()
    cur.execute(sql_v)
    return cur.fetchall()

def price_score():
    '''
    获取价格与评分
    :return:
    '''
    sql_v = '''
    SELECT
        sightName,
        qunarPrice 价格,
        ss.score 评分
    FROM
        sight_list sl
        JOIN sight_score ss ON sl.sightId = ss.sightId
    WHERE
        qunarPrice != 0
        AND sl.saleCount > 50
    ORDER BY 2 DESC
	'''
    db = test_connection()
    cur = db.cursor()
    cur.execute(sql_v)
    return cur.fetchall()

if __name__ == '__main__':
    print(province_sight_5a('湖南'))
