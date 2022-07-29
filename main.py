# main.py
# pip install sanic[ext]
# pip install sanic_session

import os,time
os.environ['TZ'] = 'Asia/Phnom_Penh'
time.tzset()

from sanic import Sanic
from config import Config
app = Sanic('Multinews')
app.static("/static", "./static")
app.config.update(Config.config)

from models.connectdb import mydb
app.ctx.mydb = mydb

from sanic_session import Session, InMemorySessionInterface
Session(app, interface=InMemorySessionInterface())

from routes.front import index
from routes.front import login
from routes.admin import admin