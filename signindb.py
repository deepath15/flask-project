import pymongo as mon

client = mon.MongoClient("mongodb://localhost")
db=client["users"]
retrivecol=db["userdata"]


def data(name,pw):
        dbdata=retrivecol.find({"username":name,"password":pw},{"_id":0})
        data_dict = {}
        for document in dbdata:
            for key, value in document.items():
                data_dict[key] = value

        
        if(data_dict):
            return data_dict
        else:
            return False

  
   

        

    
