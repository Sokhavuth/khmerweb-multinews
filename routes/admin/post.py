# routes/admin/post.py

from sanic import Sanic
from controllers.admin.post import Post
from sanic.response import redirect
 
app = Sanic.get_app('Multinews')
post = Post()
 
@app.get("/admin/post")
async def getItem(req):
    if(req.ctx.session.get('user')):
        return await post.getItem(req)
    else:
        return redirect('/login')