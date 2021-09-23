# coding: utf-8

"""
This is a recipe to import products from excel file --
1- Copy your excel file into the current folder
2- Specify your exel file path where are data to import
3- First row containes of your sheet must be culumns names, make sure columns names are in this list
*- ['dci','dosage','forme_galemique','lab_fabricant','conditionnement','prix_public']
"""

import sys
sys.path.append(r'../')
from utils import tools
import json
from db_wrapper.mongodb_wrapper import MongoWrapper
from pharmacies import tasks

def import_products(excel_file_path, sheetname: str, split_columns_values: list):
    data = tools.exel_to_json(excel_file_path, sheetname)
    data = tools.split_values(data,  split_columns_values)
    for i in range(len(data)):
        if tasks.add_product(M, data[i]) is True:
            print("produit inserer avec success")
        else:
            print("le produits n'a pas pu etre inserer")

# process
M = MongoWrapper(host='localhost', database='pharmacies')
split_columns_values = [{'key':'dci', 'separator': ','}]
import_products(r'../data/produits.xlsx', 'produits', split_columns_values)