# main.py
# pip install sanic[ext]
# pip install sanic_session[redis]

import os,time
os.environ['TZ'] = 'Asia/Phnom_Penh'
time.tzset()

from sanic import Sanic
from config import Config
app = Sanic('Multinews')
app.static("/static", "./static")
app.config.update(Config.config)

from models.connectdb import mydb, redis
app.ctx.mydb = mydb

from sanic_session import Session, RedisSessionInterface
Session(app, interface=RedisSessionInterface(redis.get_redis_pool))

from routes.front import index
from routes.front import login
from routes.admin import admin