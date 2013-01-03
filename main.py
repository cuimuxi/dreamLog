#encoding=utf-8
import web
from urls import urls
from controller import  *

web.config.debug = True
app = web.application(urls,globals(),autoreload=True)

if __name__ == "__main__":
    print 111
    app.run()