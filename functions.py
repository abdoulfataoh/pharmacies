from bson import ObjectId
from config.PRODUCTS_COLLECTION import PRODUCTS_COLLECTION_NAME, PRODUCTS_FIELDNAMES, PRODUCTS_CHECK_KEYS
from utils.tools import excel_sheet_to_json, split_values, strip_and_lowercase_values
from config.DB_CREDENTIALS import DB_URL, DB_PORT
from MongoWrapper import MongoWrapper
from config.PHARMACIES_COLLECTION import PHARMACIES_COLLECTION_NAME


### function Check if product exist
def is_product_exist(mongodb_wr: MongoWrapper, nom_commercial, conditionnement) -> dict:
    check_keys_list = PRODUCTS_CHECK_KEYS
    check_values_list = nom_commercial, conditionnement
    return mongodb_wr.is_exist(PRODUCTS_COLLECTION_NAME, check_keys_list, check_values_list)

### function Get product price
def get_prod_price(mongodb_wr: MongoWrapper, id: str) -> float:
    query = {"_id": ObjectId(id)}
    return float(mongodb_wr.get_documents(PRODUCTS_COLLECTION_NAME, query, convert_id=True)[0]['prix_public'])

## function activate a product for a pharmacy
def enable_product(mongodb_wr: MongoWrapper, pharmacy_id: str, product_id: str):
    query = { "_id": ObjectId(pharmacy_id) }
    new_values = { "$push": { "products_ids": ObjectId(product_id)  } }
    mongodb_wr.update_one(PHARMACIES_COLLECTION_NAME, query=query, new_values=new_values )
    
# function to disbale product
def disable_product(mongodb_wr: MongoWrapper, pharmacy_id: str, product_id: str):
    query = { "_id": ObjectId(pharmacy_id) }
    new_values = { "$pull": { "products_ids": ObjectId(product_id)  } }
    mongodb_wr.update_one(PHARMACIES_COLLECTION_NAME, query=query, new_values=new_values )

# function to get which min dist pharmacy has product
def which_proximities_pharmacies_have(mongodb_wr: MongoWrapper, product_id: str, longitude: float, latitude: float, limit = 20):
    query = { "products_ids": ObjectId(product_id) }
    return mongodb_wr.get_proximity_points(PHARMACIES_COLLECTION_NAME, query, longitude, latitude, limit=limit )
    

# Test
if __name__ == '__main__':
    mongo = MongoWrapper('localhost', 'pharmacies')
    # a = "61119e0156c3df8e2a7af000"
    # print(get_prod_price(mongo, a))
    # print(is_product_exist(mongo, 'leukoplast s  perf', '1/2mx18cm'))
    # disable_product(mongo, "612d7225a640a1889803d79b", "2")

    # enable_product(mongo, "612e30fed84681ac4ce2d77d", "612e3189ee3d034ebf1b2ecf")
    # enable_product(mongo, "612e30fed84681ac4ce2d77d", "612e3189ee3d034ebf1b2eb6")

    ph = which_proximities_pharmacies_have(mongo, "612e3189ee3d034ebf1b2ecf",  -1.4967793, 12.3596856, 5)
    print(ph)