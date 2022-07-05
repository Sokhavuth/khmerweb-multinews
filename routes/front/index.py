#routes/front/index.py

from sanic import Sanic
from controllers.front.index import Index
 
app = Sanic.get_app('Multinews')
 
@app.route("/")
async def index(req):
    instance = Index()
    return await instance.getItem(req)