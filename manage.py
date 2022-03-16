'''
Author: your name
Date: 2022-03-15 22:57:53
LastEditTime: 2022-03-15 23:06:27
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /flask-api/manage.py
'''
from app.app import create_app

app = create_app()

if __name__ == '__main__':
  app.run(debug=True)