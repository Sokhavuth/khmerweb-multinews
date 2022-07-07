# routes/front/login.py

from sanic import Sanic
from controllers.front.login import Login
from sanic.response import redirect
 
app = Sanic.get_app('Multinews')
instance = Login()
 
@app.get("/login")
async def getItem(req):
    if( req.ctx.session.get('user')):
        return redirect('/admin/post')
    else:
        return await instance.getItem(req)


@app.post("/login")
async def postItem(req):
    return await instance.postItem(req)


@app.get("/logout")
async def deleteItem(req):
    if(req.ctx.session.get('user')):
        return await instance.deleteItem(req)
    else:
        return redirect('/login')