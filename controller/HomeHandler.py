#encoding=utf-8
from BaseHandler import BaseHandler

class HomeHandler(BaseHandler):
    def get(self):
        self.write(u'hello 你好Demo')

