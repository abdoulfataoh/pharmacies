# -- This is a recipe to import pharmacies from excel file --


from config import DB_CREDENTIALS
from config import PHARMACIES_COLLECTION
from MongoWrapper import MongoWrapper
from utils.tools import split_values, strip_and_lowercase_values
import utils.tools

### function Insert pharmacies
def insert_pharmacy_if_not_existe(mongodb_wr: MongoWrapper, data: list):
    check_keys_list = PHARMACIES_COLLECTION.PHARMACIES_CHECK_KEYS
    check_values_list = []
    
    for pharmacy in data:
        lat = pharmacy['latitude']
        long = pharmacy['longitude']
        gps = { "type": "Point", "coordinates": [long, lat] }
        pharmacy["localisation"] = gps
        del pharmacy["latitude"]
        del pharmacy["longitude"]
        pharmacy["products_ids"] = []
        for k in check_keys_list:
            check_values_list.append(pharmacy[k])  
        if mongodb_wr.insert_if_not_exist(PHARMACIES_COLLECTION.PHARMACIES_COLLECTION_NAME, check_keys_list, check_values_list, pharmacy ) is True:
            n = pharmacy['nom_pharmacie']
            # print(f'{n} inserer avec success')
        else:
            n = pharmacy['nom_pharmacie']
            print(f'{n} existe deja')
        check_values_list = []
    print(f' ----------done {len(data)}--------')
   



mongo = MongoWrapper(host=DB_CREDENTIALS.DB_URL, database=DB_CREDENTIALS.DB_NAME )

# Specify your sheetname where are data to import
filepath = r'data/pharmacies.xlsx'
sheetname = 'pharmacies'

data = utils.tools.excel_sheet_to_json(path=filepath,  sheetname=sheetname)
fields_to_split = [{'key':'addresse', 'separator': ','}]
data = split_values(data, fields_to_split)
data = strip_and_lowercase_values(data)
insert_pharmacy_if_not_existe(mongo, data)