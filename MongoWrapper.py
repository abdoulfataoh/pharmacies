from typing import Dict
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
    def inserts_into_collection(self, collection, documents):
        col = self.db[collection]
        col.insert_many(documents)

    def insert_one_into_collection(self, collection, document):
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

    # Check if a value existe on db
    def is_exist(self, collection: str, keys_list: list, values_list : list) -> bool:  
        if len(keys_list) != len(values_list):
            raise Exception("le nombre de cles est different du nombre de valeurs transmins")
        else:
            filter = dict(zip(keys_list, values_list))
            qry_result = self.get_documents(collection, query=filter)
        if len(qry_result) > 0:
            return True
        else:
            return False

    # Insert doc if not exist
    def insert_if_not_exist(self, collection: str, check_keys_list: list, check_values_list, document: dict):
        if self.is_exist(collection, check_keys_list, check_values_list) is False:
            self.insert_one_into_collection(collection=collection, document=document)
            return True
        else:
            return False

    # Test
    def test(self):
        return (self.conn.list_database_names())
