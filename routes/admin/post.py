# routes/admin/post.py

from sanic import Sanic
from controllers.admin.post import Post
 
app = Sanic.get_app('Multinews')
instance = Post()
 
@app.get("/admin/post")
async def getItem(req):
    return await instance.getItem(req)