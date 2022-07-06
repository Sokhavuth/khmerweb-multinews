# main.py
# pip install sanic[ext]

import os,time
from sanic import Sanic
from config import Config

os.environ['TZ'] = 'Asia/Phnom_Penh'
time.tzset()
 
app = Sanic('Multinews')
app.static("/static", "./static")
app.config.update(Config.config)
 
from routes.front import index