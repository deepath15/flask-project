import pymongo as mon

client = mon.MongoClient("mongodb://localhost:27017")
db=client["resume"]
col=db["login"]

