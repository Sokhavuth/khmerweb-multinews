# routes/front/login.py

from sanic import Sanic
from controllers.front.login import Login
 
app = Sanic.get_app('Multinews')
 
@app.route("/login")
async def getItem(req):
    instance = Login()
    return await instance.getItem(req)