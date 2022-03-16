'''
Author: your name
Date: 2022-03-15 22:52:24
LastEditTime: 2022-03-15 23:34:36
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /flask-api/app/app.py
'''
from flask import Flask

from app.api.v1 import create_blueprint_v1


def register_blueprints(app):
  app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')

def create_app():
  app = Flask(__name__)
  app.config.from_object('app.config.secure')
  app.config.from_object('app.config.setting')
  register_blueprints(app)
  return app