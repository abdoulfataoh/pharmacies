# coding: utf-8

# Products collection config
PRODUCTS_COLLECTION_NAME = 'products_listing'
PRODUCTS_KEYS_NAMES = [
    'nom_commercial',
    'dci',
    'dosage',
    'forme_galemique',
    'lab_fabricant',
    'conditionnement',
    'prix_public'
]

PRODUCTS_CHECK_KEYS = ['nom_commercial', 'conditionnement']

# Pharmacies collection config
PHARMACIES_COLLECTION_NAME = 'pharmacies_listing'
PHARMACIES_KEYS_NAMES = [
    "nom_pharmacie",
    "telephone",
    "addresse",
    "code_postale",
    "assurance",
    "groupe",
    "localisation",
    "products_ids"
]
PHARMACIES_CHECK_KEYS = ['nom_pharmacie',  'addresse']

