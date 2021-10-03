import connexion
import six
from datetime import datetime
import sys
sys.path.append(r'../')

from swagger_server.models.pharmacie_add_body import PharmacieAddBody  # noqa: E501
from swagger_server.models.pharmacie_id_set_available_products_body import PharmacieIdSetAvailableProductsBody  # noqa: E501
from swagger_server.models.pharmacie_id_set_unvailable_products_body import PharmacieIdSetUnvailableProductsBody  # noqa: E501
from swagger_server.models.products_add_body import ProductsAddBody  # noqa: E501
from swagger_server.models.search_pharmacies_body import SearchPharmaciesBody  # noqa: E501
from swagger_server import util

from pharmacies import tasks
from db_wrapper import mongodb_wrapper

host='localhost'
database='pharmacies'
port=27017

def result_model(success, result):
    return  {
            "success": success,
            "timestamp": datetime.now(),
            "result": result
    }

M = mongodb_wrapper.MongoWrapper(host=host, database=database, port=port)


def health_get():  # noqa: E501
    r = tasks.health(M)
    if r == True:
        return result_model(True, r)
    else:
        return result_model(False, r)



def pharmacie_add_post(body):  # noqa: E501
    """add a pharmacie

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: object
    """
    if connexion.request.is_json:
        body = PharmacieAddBody.from_dict(connexion.request.get_json())  # noqa: E501
        body = body.to_dict()
        r = tasks.add_pharmacie(M, body)
    return result_model("", r)


def pharmacie_pharmacie_id_delete(pharmacie_id):  # noqa: E501
    """delete a pharmacie by id

     # noqa: E501

    :param pharmacie_id: 
    :type pharmacie_id: str

    :rtype: object
    """
    r = tasks.delete_pharmacie(M, pharmacie_id)
    return result_model("", r)


def pharmacies_list_get():  # noqa: E501
    """Returns a list of pharmacies

     # noqa: E501


    :rtype: object
    """
    r = tasks.get_pharmacies(M)
    return result_model("True", r)


def pharmacies_manager_pharmacie_id_set_unvailable_products_post(body, pharmacie_id):  # noqa: E501
    """set products list as available products for a pharmacie

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param pharmacie_id: pharmacie_id
    :type pharmacie_id: str

    :rtype: object
    """
    if connexion.request.is_json:
        body = PharmacieIdSetUnvailableProductsBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def pharmacies_mananger_pharmacie_id_set_available_products_post(body, pharmacie_id):  # noqa: E501
    """set products list as available products for a pharmacie

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param pharmacie_id: pharmacie_id
    :type pharmacie_id: str

    :rtype: object
    """
    if connexion.request.is_json:
        body = PharmacieIdSetAvailableProductsBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def pharmacies_proximities_list_get(lat, long):  # noqa: E501
    """Returns a list of pharmacies order by proximity

     # noqa: E501

    :param lat: client location latitude
    :type lat: float
    :param long: client location longitude
    :type long: float

    :rtype: object
    """
    return 'do some magic!'


def pharmacies_proximities_search_product_id_post(body, search_product_id):  # noqa: E501
    """Returns a list of pharmacies order by proximity with a specic product

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param search_product_id: product id
    :type search_product_id: str

    :rtype: object
    """
    if connexion.request.is_json:
        body = SearchPharmaciesBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'



#########################################################3
def products_add_post(body):  # noqa: E501
    """add a product

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: object
    """
    if connexion.request.is_json:
        body = ProductsAddBody.from_dict(connexion.request.get_json())  # noqa: E501
        body = body.to_dict()
        r = tasks.add_product(M, body)
    return result_model("", r)

def products_list_get():  # noqa: E501
    """Returns a list of products

     # noqa: E501


    :rtype: object
    """
    r = tasks.get_products(M)
    return result_model("", r)


def products_product_id_delete(product_id):  # noqa: E501
    """delete a product

     # noqa: E501

    :param product_id: 
    :type product_id: str

    :rtype: object
    """
    r = tasks.delete_product(M,  product_id)
    return result_model("", r)
