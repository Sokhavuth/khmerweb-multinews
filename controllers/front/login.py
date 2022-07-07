# controllers/front/login.py

from sanic import Sanic
from sanic_ext import render

class Login():
    def __init__(self):
        app = Sanic.get_app('Multinews')
        self.config = app.config

    async def getItem(self,req):
        self.config["pageTitle"] = 'ទំព័រ​ចុះ​ឈ្មោះ​ចូល​​ក្នុង'
        self.config['route'] = '/login'

        return await render("base.html", context={"data":self.config})