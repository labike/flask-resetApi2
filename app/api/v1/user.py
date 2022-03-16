'''
Author: your name
Date: 2022-03-15 23:05:44
LastEditTime: 2022-03-15 23:33:02
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /flask-api/app/api/v1/user.py
'''
from flask import Blueprint

from app.libs.redprint import Redprint

# user = Blueprint('user', __name__)
api = Redprint('user')

@api.route('/get')
def get_user():
  return 'i am koa'