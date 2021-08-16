from itertools import product
from pymongo.message import insert
from utils.tools import excel_sheet_to_json, split_values, strip_and_lowercase_values
from config.DB_CREDENTIALS import DB_URL, DB_PORT
from MongoWrapper import MongoWrapper

### function Insert one by one product with check if product dosent existe
def insert_prod_if_not_existe(mongodb_wr: MongoWrapper, data: list):
    check_keys_list = 'nom_commercial', 'conditionnement'
    check_values_list = []
    for product in data:
        for k in check_keys_list:
            check_values_list.append(product[k])
        if mongodb_wr.insert_if_not_exist('products_listing', check_keys_list, check_values_list, product ) is True:
            print('inserer avec success')
        else:
            print('existe deja')
        check_values_list = []


### function Check if product exist
def is_prod_exist(mongodb_wr: MongoWrapper, nom_commercial, conditionnement) -> dict:
    check_keys_list = 'nom_commercial', 'conditionnement'
    check_values_list = nom_commercial, conditionnement
    return mongodb_wr.is_exist('products_listing', check_keys_list, check_values_list)

### function Get product price
def get_prod_price(mongodb_wr: MongoWrapper, nom_commercial, conditionnement) -> dict:
    check_keys_list = 'nom_commercial', 'conditionnement'
    check_values_list = nom_commercial, conditionnement
    filter = dict(zip(check_keys_list, check_values_list))
    return float(mongodb_wr.get_documents('products_listing', filter, {"_id": 0, "prix_public": 1})[0]["prix_public"])



### Main
db = 'pharmacies'
collection = 'products_listing'

# Instance db Mongo_wrapper object
mongodb_wr = MongoWrapper(host=DB_URL, port=DB_PORT, database=db)

# Read and format data from excel sheets
data = excel_sheet_to_json("data/Listing produits Phcie  Georgette.xlsx", "Base de données détaillées")
fields_to_split = [{'key':'dci', 'separator': ','}]
data = split_values(data, fields_to_split)
data = strip_and_lowercase_values(data)

### Example: Insert Products on db without control
# mongodb_wr.inserts_into_collection(collection, data)

### Insert with control
insert_prod_if_not_existe(mongodb_wr, data)

### EXample: check if product exist
print(is_prod_exist(mongodb_wr, 'leukoplast s  perf', '1/2mx18cm'))

print(get_prod_price(mongodb_wr, 'leukoplast s  perf', '1/2mx18cm'))
# print(mongodb_wr.get_documents())