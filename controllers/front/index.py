# controllers/front/index.py
# pip install sanic[ext]

from config import setting
from sanic_ext import render

class Index():
    async def getItem(self,req):
        self.config = await setting()
        self.config["pageTitle"] = 'ទំព័រ​ដើម'
        self.config['route'] = '/'
        self.config['message'] = 'កម្មវិធី​គេហទំព័រ​ ពហុដំណឹង កំពុង​រៀបចំ​បង្កើត!'

        return await render("base.html", context={"data":self.config})
