from bson import ObjectId
from config.PRODUCTS_COLLECTION import PRODUCTS_COLLECTION_NAME, PRODUCTS_FIELDNAMES, PRODUCTS_CHECK_KEYS
from utils.tools import excel_sheet_to_json, split_values, strip_and_lowercase_values
from config.DB_CREDENTIALS import DB_URL, DB_PORT
from MongoWrapper import MongoWrapper



### function Insert one by one product with check if product dosent existe
def insert_product_if_not_existe(mongodb_wr: MongoWrapper, data: list):
    check_keys_list = PRODUCTS_CHECK_KEYS
    check_values_list = []
    for product in data:
        for k in check_keys_list:
            check_values_list.append(product[k])
        if mongodb_wr.insert_if_not_exist(PRODUCTS_COLLECTION_NAME, check_keys_list, check_values_list, product ) is True:
            print('inserer avec success')
        else:
            print('existe deja')
        check_values_list = []


### function Check if product exist
def is_product_exist(mongodb_wr: MongoWrapper, nom_commercial, conditionnement) -> dict:
    check_keys_list = PRODUCTS_CHECK_KEYS
    check_values_list = nom_commercial, conditionnement
    return mongodb_wr.is_exist(PRODUCTS_COLLECTION_NAME, check_keys_list, check_values_list)

### function Get product price
def get_prod_price(mongodb_wr: MongoWrapper, id: str) -> float:
    query = {"_id": ObjectId(id)}
    return float(mongodb_wr.get_documents(PRODUCTS_COLLECTION_NAME, query, convert_id=True)[0]['prix_public'])

# Test
if __name__ == '__main__':
    mongo = MongoWrapper('localhost', 'pharmacies')
    # a = "61119e0156c3df8e2a7af000"
    # print(get_prod_price(mongo, a))
    print(is_product_exist(mongo, 'leukoplast s  perf', '1/2mx18cm'))