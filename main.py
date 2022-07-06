# main.py
# pip install sanic[ext]
# pip install python-dotenv

import os,time
os.environ['TZ'] = 'Asia/Phnom_Penh'
time.tzset()

from sanic import Sanic
from config import Config
app = Sanic('Multinews')
app.static("/static", "./static")
app.config.update(Config.config)

from models.connectdb import Database
app.ctx.mydb = Database.mydb

from routes.front import index