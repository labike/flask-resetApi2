'''
Author: your name
Date: 2022-03-15 23:19:11
LastEditTime: 2022-03-16 10:22:32
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /flask-api/app/libs/redprint.py
'''
from click import option


class Redprint:
  def __init__(self, name):
    self.name = name
    self.mound = [] # 保存向blueprint注册时的参数

  def route(self, rule, **options):
    def decorator(fn):
      self.mound.append((fn, rule, options))
      return fn

    return decorator

  def register(self, bp, url_prefix = None):
    if url_prefix is None:
      url_prefix = '/' + self.name
    # options是dic类型, <type dic>.pop()表示获取字典里的某个值并将其删除
    # 由于options中可能没有endpoint, 所以需要以当前视图函数的名字作为默认值
    for fn, rule, options in self.mound:
      endpoint = options.pop('endpoint', fn.__name__)
      bp.add_url_rule(url_prefix + rule, endpoint, fn, **options)