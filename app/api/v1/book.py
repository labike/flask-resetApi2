'''
Author: your name
Date: 2022-03-15 23:05:52
LastEditTime: 2022-03-15 23:32:55
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /flask-api/app/api/v1/book.py
'''
from flask import Blueprint

from app.libs.redprint import Redprint

book = Blueprint('book', __name__)
api = Redprint('book')

@api.route('/get')
def get_book():
  return 'get book'

@api.route('/create')
def create_book():
  return 'create book'