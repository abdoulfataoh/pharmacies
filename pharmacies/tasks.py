# coding: utf-8

import sys
sys.path.append(r'../')
import json
from pharmacies import settings
from db_wrapper.mongodb_wrapper import MongoWrapper
from bson import ObjectId

def health(mongodb_wrapper: MongoWrapper) -> bool:
    try:
        mongodb_wrapper.test()
        return True
    except:
        return False


def add_product(db_wrapper: MongoWrapper, product: dict) -> bool:
    """add a product to the database"""
    if _is_valide_structure(list(product.keys()), settings.PRODUCTS_KEYS_NAMES) is True:
        return db_wrapper.insert_if_not_exist(collection=settings.PRODUCTS_COLLECTION_NAME,
                    check_keys=settings.PRODUCTS_CHECK_KEYS,
                    document=product
        )
    else:
        return False

def get_products(db_wrapper: MongoWrapper):
    """ get all products list"""
    d = db_wrapper.get_documents(collection=settings.PRODUCTS_COLLECTION_NAME)   
    return _decode_ids(d, ["_id"])
    

def edit_product(db_wrapper: MongoWrapper, product_id: str, set_document: dict):
    """ modify an existing product """
    if _is_valide_structure(list(set_document.keys()), settings.PRODUCTS_KEYS_NAMES) is True:
        set_document = { "$set": set_document }
        db_wrapper.update_document(collection=settings.PRODUCTS_COLLECTION_NAME,
                            set_document=set_document
        )
    else:
        return False

def delete_product(db_wrapper: MongoWrapper, product_id: str):
    """delete a product by _id"""
    db_wrapper.delete_document(collection=settings.PRODUCTS_COLLECTION_NAME, filter={"_id": ObjectId(product_id)})
    return True

def add_pharmacie(db_wrapper: MongoWrapper, pharmacie: dict) -> bool:
    """add a pharmacie to the database"""
    if _is_valide_structure(list(pharmacie.keys()), settings.PHARMACIES_KEYS_NAMES) is True:
        return db_wrapper.insert_if_not_exist(collection=settings.PHARMACIES_COLLECTION_NAME,
                    check_keys=settings.PHARMACIES_CHECK_KEYS,
                    document=pharmacie
        )
    else:
        return False

def get_pharmacies(db_wrapper: MongoWrapper):
    """ get all pharmacies list"""
    d = db_wrapper.get_documents(collection=settings.PHARMACIES_COLLECTION_NAME)
    return _decode_ids(d, ["_id", "products_ids"])  

def edit_pharmacie(db_wrapper: MongoWrapper, pharmacie_id: str, set_document: dict):
    """ modify an existing pharmacie """
    if _is_valide_structure(list(set_document.keys()), settings.PHARMACIES_KEYS_NAMES) is True:
        set_document = { "$set": set_document }
        db_wrapper.update_document(collection=settings.PHARMACIES_COLLECTION_NAME,
                            set_document=set_document
        )
    else:
        return False

def delete_pharmacie(db_wrapper: MongoWrapper, pharmacie_id: str):
    db_wrapper.delete_document(collection=settings.PHARMACIES_COLLECTION_NAME, filter={"_id": ObjectId(pharmacie_id)})
    return True

def _is_valide_structure(keys: list, check_keys: list) -> bool:
    if len(keys) == len(check_keys):
        return any([keys[i] in check_keys for i in range(len(keys)) ])
    else:
        return False

def _decode_ids(documents: list, keys) -> list:
    for doc in documents:
        for k in keys:
            try:
                doc[k] = [ str(v) for v in doc[k] ]
            except TypeError:
                doc[k]= str(doc[k])
    return documents

def enable_product(mongodb_wr: MongoWrapper, pharmacy_id: str, product_id: str):
    """activate a product for a pharmacy"""
    filter = { "_id": ObjectId(pharmacy_id) }
    new_values = { "$push": { "products_ids": ObjectId(product_id)  } }
    mongodb_wr.update_document(settings.PHARMACIES_COLLECTION_NAME, filter=filter, set_document=new_values )
    
def disable_product(mongodb_wr: MongoWrapper, pharmacy_id: str, product_id: str):
    """disbale product"""
    filter = { "_id": ObjectId(pharmacy_id) }
    new_values = { "$pull": { "products_ids": ObjectId(product_id)  } }
    mongodb_wr.update_document(settings.PHARMACIES_COLLECTION_NAME, filter=filter, set_document=new_values )

def search_pharmacies(mongodb_wr: MongoWrapper,groupe, product_id: str, longitude: float, latitude: float, limit = 20):
    try:
        query = { "products_ids": ObjectId(product_id), "groupe": groupe }
    except:
        return {}
    d = mongodb_wr.get_proximity_points(settings.PHARMACIES_COLLECTION_NAME, query, longitude, latitude, limit=limit)
    return _decode_ids(d, ["_id"])   

# Test
if __name__ == '__main__':
    M = MongoWrapper(host='localhost', database='pharmacies')
    # print(add_product(M, {"a":4, "b": 4}))
    # print(get_products(M))
    # delete_product(M, "614b1dc0c1b00b1b89acadc0")
    # enable_product(M, "614c67ec7831965969347dc6", "614b9bbe257b7ec7226aad2d")
    # d = search_pharmacies(M, "groupe 1", "614b9bbe257b7ec7226aad2d", -1.5698727, 12.3330991, 5)
    print(add_product(M, {}))
    