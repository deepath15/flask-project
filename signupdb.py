import pymongo as mon

client = mon.MongoClient("mongodb://localhost")
db=client["users"]
col=db["userdata"]

