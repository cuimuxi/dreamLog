#encoding=utf8
import os

setting = dict(
    blog_title=u"Tornado Blog",
    template_path=os.path.join(os.path.dirname(__file__), "view"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    xsrf_cookies=True,
    cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
    login_url="/auth/login",
    autoescape=None,
    debug=True,
)