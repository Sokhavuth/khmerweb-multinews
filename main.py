# main.py

import os,time
from sanic import Sanic

os.environ['TZ'] = 'Asia/Phnom_Penh'
time.tzset()
 
app = Sanic('Multinews')
app.static("/static", "./static")
 
from routes.front import index