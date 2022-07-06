# controllers/front/index.py

from sanic import Sanic
from sanic_ext import render

class Index():
    def __init__(self):
        app = Sanic.get_app('Multinews')
        self.config = app.config

    async def getItem(self,req):
        self.config["pageTitle"] = 'ទំព័រ​ដើម'
        self.config['route'] = '/'
        self.config['message'] = 'កម្មវិធី​គេហទំព័រ​ ពហុដំណឹង កំពុង​រៀបចំ​បង្កើត!'

        return await render("base.html", context={"data":self.config})
