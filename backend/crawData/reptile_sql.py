import pymysql

db = pymysql.connect(host='localhost',user='root',password='1234CDcd',database='travel_flask')
cur = db.cursor()


def insert_sight_list(data):
    sql_v = '''
    REPLACE INTO `travel_flask`.`sight_list` (`score`, `sightId`, `intro`, `free`, `point`, `address`, `sightName`, `districts`, `saleCount`, `qunarPrice`, `star`, `province`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    '''
    try:
        cur.execute(sql_v,data)
        db.commit()
    except:
        db.rollback()
        raise Exception('数据插入错误')

def insert_province_sight_subjects(data):
        sql_v = '''
        REPLACE INTO `travel_flask`.`province_sight_subjects` (`province`, `subjects`, `count`, `key`) VALUES (%s, %s, %s, %s)
        '''
        try:
            cur.execute(sql_v,data)
            db.commit()
        except:
            db.rollback()
            raise Exception('数据插入错误')


def insert_sight_score(data):
    sql_v = '''
    REPLACE
    INTO
    `travel_flask`.
    `sight_score`(`sightId`, `score`, `commentCount`)
    VALUES(%s,%s,%s)
    '''
    try:
        cur.execute(sql_v, data)
        db.commit()
    except:
        db.rollback()
        raise Exception('数据插入错误')




