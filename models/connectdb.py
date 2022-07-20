# models/connectdb.py
# pip install python-dotenv
# pip install motor

import os
from dotenv import load_dotenv  
load_dotenv()

import asyncio
import motor.motor_asyncio

mydb = None

async def get_server_info():
    global mydb
    conn_str = os.getenv('DATABASE_URI')
    client = motor.motor_asyncio.AsyncIOMotorClient(conn_str, serverSelectionTimeoutMS=5000)
    mydb = client[os.getenv('DB_NAME')]
    
loop = asyncio.get_event_loop()
loop.run_until_complete(get_server_info())