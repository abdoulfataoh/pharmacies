# -- This is a recipe to import products from excel file --
#  1- Copy your excel file into the current folder
#  2- Specify your exel file path where are data to import
#  3- First row containes of your sheet must be culumns names, make sure columns names are in this list
#  *- ['dci','dosage','forme_galemique','lab_fabricant','conditionnement','prix_public']

from config import DB_CREDENTIALS
from config import PRODUCTS_COLLECTION
from MongoWrapper import MongoWrapper
from utils.tools import split_values, strip_and_lowercase_values
import utils.tools

### function Insert one by one product with check if product dosent existe
def insert_product_if_not_existe(mongodb_wr: MongoWrapper, data: list):
    check_keys_list = PRODUCTS_COLLECTION.PRODUCTS_CHECK_KEYS
    check_values_list = []
    for product in data:
        for k in check_keys_list:
            check_values_list.append(product[k])
        if mongodb_wr.insert_if_not_exist(PRODUCTS_COLLECTION.PRODUCTS_COLLECTION_NAME, check_keys_list, check_values_list, product ) is True:
            print('inserer avec success')
        else:
            print('existe deja')
        check_values_list = []

mongo = MongoWrapper(host=DB_CREDENTIALS.DB_URL, database=DB_CREDENTIALS.DB_NAME )

# Specify your sheetname where are data to import
filepath = r'data/produits.xlsx'
sheetname = 'produits'

data = utils.tools.excel_sheet_to_json(path=filepath,  sheetname=sheetname)
fields_to_split = [{'key':'dci', 'separator': ','}]
data = split_values(data, fields_to_split)
data = strip_and_lowercase_values(data)
insert_product_if_not_existe(mongo, data)