# coding: utf-8
"""
This is a recipe to import pharmacies from excel file --
"""

import sys
sys.path.append(r'../')
from utils import tools
import json
from db_wrapper.mongodb_wrapper import MongoWrapper
from pharmacies import tasks

M = MongoWrapper(host='localhost', database='pharmacies')


def import_pharmacies(excel_file_path, sheetname: str, split_columns_values: list):
    data = tools.exel_to_json(excel_file_path, sheetname)
    data = tools.split_values(data,  split_columns_values)
    data = [_format_pharmacie(d) for d in data]
    for i in range(len(data)):
        if tasks.add_pharmacie(M, data[i]) is True:
            print("pharmacie inserer avec success")
        else:
            print("la pharmacie n'a pas pu etre inserer")

def _format_pharmacie(pharmacie: str) -> dict:
        pharmacie["products_ids"] = []
        latitude = float(pharmacie['latitude'])
        longitude = float(pharmacie['longitude'])
        gps = { "type": "Point", "coordinates": [latitude, longitude] }
        pharmacie["localisation"] = gps
        del pharmacie["latitude"]
        del pharmacie["longitude"]
        return pharmacie

# process
split_columns_values = [{'key':'assurance', 'separator': ','}]
import_pharmacies(r'../data/groupes_pharmacies.xlsx', 'groupe_4', split_columns_values)
