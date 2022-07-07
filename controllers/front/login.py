# controllers/front/login.py
# pip install bcrypt

from sanic import Sanic
from sanic_ext import render
from copy import deepcopy
import bcrypt,uuid
from sanic.response import redirect

class Login():
    def __init__(self):
        app = Sanic.get_app('Multinews')
        self.config = deepcopy(app.config)
        self.mydb = app.ctx.mydb


    async def getItem(self,req):
        self.config["pageTitle"] = 'ទំព័រ​ចុះ​ឈ្មោះ​ចូល​​ក្នុង'
        self.config['route'] = '/login'

        return await render("base.html", context={"data":self.config})


    async def createRootUser(self):
        password = b"xxxxxxxxxxxxxxx"
        hashedPassword = bcrypt.hashpw(password, bcrypt.gensalt())

        user = { 
            "id": uuid.uuid4().hex, 
            "email": "root@khmerweb.app",
            "username": "Sokhavuth",
            "password": hashedPassword,
            "role":"Admin",
            "thumb":"",
            "info":"",
            "video":"",
            "date":""
        }
        
        self.mydb['users'].insert_one(user)


    async def postItem(self,req):
        email = req.form.get('email')
        password = req.form.get('password')

        user = self.mydb['users'].find_one({'email':email})
        
        if user:
            if(bcrypt.checkpw(password.encode('utf-8'), user['password'])):
                self.config["pageTitle"] = 'ទំព័រ​ការផ្សាយ'
                req.ctx.session['user'] = {'id':user['id'],'role':user['role']}
                return redirect('/admin/post')
            else:
                self.config['message'] = 'ពាក្យ​សំងាត់របស់អ្នក​​មិន​ត្រឹមត្រូវ​ទេ!'
                return await render("base.html", context={"data":self.config})
        else:
            self.config['message'] = 'Email របស់​អ្នក​មិន​ត្រឹមត្រូវ​ទេ!'
            return await render("base.html", context={"data":self.config})


    async def deleteItem(self,req):
        req.ctx.session['user'] = None
        return redirect('/')