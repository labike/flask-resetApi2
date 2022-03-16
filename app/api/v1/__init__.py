'''
Author: your name
Date: 2022-03-15 23:05:21
LastEditTime: 2022-03-16 10:23:04
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /flask-api/app/api/v1/__init__.py
'''
from flask import Blueprint
from app.api.v1 import user, book


def create_blueprint_v1():
  bp_v1 = Blueprint('v1', __name__)
  user.api.register(bp_v1)
  book.api.register(bp_v1)
  return bp_v1