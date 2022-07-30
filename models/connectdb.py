# models/connectdb.py
# pip install python-dotenv
# pip install motor

import os
from dotenv import load_dotenv  
load_dotenv()

import asyncio
import motor.motor_asyncio
import asyncio_redis

mydb = None

async def get_server_info():
    global mydb
    conn_str = os.getenv('DATABASE_URI')
    client = motor.motor_asyncio.AsyncIOMotorClient(conn_str, serverSelectionTimeoutMS=5000)
    mydb = client[os.getenv('DB_NAME')]
    
loop = asyncio.get_event_loop()
loop.run_until_complete(get_server_info())

class Redis:
    """
    A simple wrapper class that allows you to share a connection
    pool across your application.
    """
    _pool = None

    async def get_redis_pool(self):
        if not self._pool:
            self._pool = await asyncio_redis.Pool.create(
                host=os.getenv('REDIS_URI'), port=int(os.getenv('REDIS_PORT')), 
                password=os.getenv('REDIS_PASSWORD'), poolsize=10
            )

        return self._pool


redis = Redis()