# -*- codeing = utf-8 -*-
# @Author: zhangfan
# @File: wholeClass.py
# @Software: PyCharm

# 创建数据库中的表
from exts import db

# __tablename__ 的值需要全小写
class Test(db.Model):
    __tablename__ = "test"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)

    # 模型的资源序列化函数
    def test_schema(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
        }


# 热门城市下的热门景点
class HotCityPlace(db.Model):
    __tablename__ = "hotcityplace"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ctiyName = db.Column(db.String(200), nullable=False)
    placeName = db.Column(db.String(200), nullable=True)

    # 模型的资源序列化函数
    def schema(self):
        return {
            "id": self.id,
            "ctiyName": self.ctiyName,
            "placeName": self.placeName
        }

# 各省份推荐的景区
class ProvinceScenic(db.Model):
    __tablename__ = "provincescenic"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    provinceName = db.Column(db.String(200), nullable=False)
    ScenicName = db.Column(db.String(200), nullable=True)
    ticketsNum = db.Column(db.String(200), nullable=True)
    # 模型的资源序列化函数
    def schema(self):
        return {
            "id": self.id,
            "provinceName": self.provinceName,
            "ScenicName": self.ScenicName,
            "ticketsNum": self.ticketsNum
        }


# 各省份的5A景区
class Scenic5A(db.Model):
    __tablename__ = "scenic5a"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    provinceName = db.Column(db.String(200), nullable=False)
    Scenic5AName = db.Column(db.String(200), nullable=True)

    # 模型的资源序列化函数
    def schema(self):
        return {
            "id": self.id,
            "provinceName": self.provinceName,
            "Scenic5AName": self.Scenic5AName
        }


#  各省份景区分类
class ScenicType(db.Model):
    __tablename__ = "scenictype"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    provinceName = db.Column(db.String(200), nullable=False)
    ScenicType = db.Column(db.String(200), nullable=False)
    ScenicNum = db.Column(db.String(200), nullable=False)

    # 模型的资源序列化函数
    def schema(self):
        return {
            "id": self.id,
            "provinceName": self.provinceName,
            "Scenic5AName": self.Scenic5AName,
            "ScenicNum": self.ScenicNum
        }


