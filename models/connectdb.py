# models/connectdb.py
# pip install python-dotenv
# pip install pymongo

import os
from dotenv import load_dotenv  
load_dotenv()
import pymongo

class Database():
    myclient = pymongo.MongoClient(os.getenv('DATABASE_URI'))
    mydb = myclient[os.getenv('DB_NAME')]