# -*- codeing = utf-8 -*-
# @Author: zhangfan
# @File: chinaMap.py
# @Software: PyCharm

from flask import Blueprint
import sys
sys.path.append("..")
import web_sql




bp = Blueprint('chinaMap', __name__, url_prefix="/v1/apis/chinaMap")

# 测试接口
@bp.route('/')
def test():
    return "测试基地址接口/v1/apis/chinaMap"

# 中国各省份的游客量
@bp.route('/touristNumber', methods=['POST','GET'])
def get_china_tourist_number():
    return "中国各省份的游客量"

# 中国各省份的景区数量
@bp.route('/scenicNumber', methods=['POST','GET'])
def get_china_scenic_number():
    return "中国各省份的景区数量"

