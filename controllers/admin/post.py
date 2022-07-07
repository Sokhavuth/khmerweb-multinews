# controllers/admin/post.py

from sanic import Sanic
from sanic_ext import render
from copy import deepcopy

class Post():
    def __init__(self):
        app = Sanic.get_app('Multinews')
        self.config = deepcopy(app.config)


    async def getItem(self,req):
        self.config["pageTitle"] = 'ទំព័រ​ការផ្សាយ'
        self.config['route'] = '/admin/post'
        self.config['type'] = 'post'

        return await render("base.html", context={"data":self.config})