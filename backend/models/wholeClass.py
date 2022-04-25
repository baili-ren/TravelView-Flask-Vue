# -*- codeing = utf-8 -*-
# @Author: zhangfan
# @File: wholeClass.py
# @Software: PyCharm

# 创建数据库中的表
from exts import db


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
            "password": self.password
        }


