# 数据库的配置变量
HOSTNAME = 'localhost'
PORT     = '3306'
DATABASE = 'travel_flask'
USERNAME = 'root'
PASSWORD = '1234CDcd'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True

