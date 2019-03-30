#所有可以被访问的urls列表
from .views import *

urls = [
        ('/time',show_time),
        ('/hello',say_hello),
        ('/bye',say_say)
        ]