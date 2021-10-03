from typing import Dict
from bson.objectid import ObjectId
from pymongo import MongoClient, collection, database, hello

class MongoWrapper(object):
    conn = None
    db = None

    # constructor definition
    def __init__(self, host, database: str, port= 27017, username=None, password=None) -> None:
        super().__init__()
        self.conn = MongoClient(host=host, port=port)
        self.db = self.conn[database]
        if username is not None or password is not None:
            self.db.authenticate(username, password)

    # definition of db insertion method
    def insert_documents(self, collection, documents):
        col = self.db[collection]
        col.insert_many(documents)

    def insert_document(self, collection, document):
        col = self.db[collection]
        col.insert_one(document)
         
    # definition of get documents list from collection
    def get_documents(self, collection, query={}, projection=None) -> list:
        col = self.db[collection]
        if projection is None:
            cursor = col.find(query)
        else:
            cursor = col.find(query, projection)
        docs_list = []
        for doc in cursor:
            docs_list.append(doc)
        return docs_list
  
        
    # function proximity points
    def get_proximity_points(self,collection: str, query: dict, latitude: float, longitude: float, limit = 20, raduis=274_200_000):
        col = self.db[collection]
        pipeline = [
            {
                "$geoNear": {
                    "near": { "type": "Point", "coordinates": [latitude, longitude] },
                    "key": "localisation",
                    "distanceField": "distance",
                    "query": query,
                    "maxDistance": raduis
                }
            },
            { "$limit": limit },
            { "$sort" : { "distance" : 1 } }
        ]
        return [doc for doc in col.aggregate(pipeline)]

    # Update one document
    def update_document(self, collection: str, filter, set_document: dict):
        col = self.db[collection]
        col.update_one(filter, set_document)
    

    # Check if a value existe on db
    def is_exist(self, collection: str, check_keys: list, document) -> bool:
        try:
            tmp_dic = {}
            for key in check_keys:
                tmp_dic[key] = document[key]
        except KeyError:
            return False
        else:
            filter = tmp_dic
            if filter == {}:
                return False
            qry_result = self.get_documents(collection, query=filter)
            return True if len(qry_result) > 0 else False

    # Insert doc if not exist
    def insert_if_not_exist(self, collection: str, check_keys: list, document: dict) -> bool:
        if self.is_exist(collection, check_keys, document) is False:
            self.insert_document(collection=collection, document=document)
            return True
        else:
            return False

    # delete document from _id
    def delete_document(self, collection: str, filter):
         col = self.db[collection]
         col.delete_one(filter)    

    def test(self):
        return (self.conn.list_database_names())
 
# Test
if __name__ == '__main__':
    M = MongoWrapper(host='localhost', database='pharmacies')
    # print(mongo.test())
    # d = mongo.get_documents('products_listing', query={}, convert_id=True)
    # print(d)
    d = M.get_proximity_points('pharmacies_listing', {} ,  -1.5698727, 12.3330991)
    print(d)
    # print(M.is_exist("test", ["a", "b"], {"a":1, "b": 2}))
    # d = {"a":1, "b": 4}
    # print(M.insert_if_not_exist("test", ["a", "b"], d) )