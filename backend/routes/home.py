# -*- codeing = utf-8 -*-
# @Author: zhangfan
# @File: home.py
# @Software: PyCharm

from flask import Blueprint
bp = Blueprint('home_bp', __name__)


@bp.route('/home', methods=['GET', 'POST'])
def home_info():
    return "home"

