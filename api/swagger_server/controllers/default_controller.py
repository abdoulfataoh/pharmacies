import connexion
import six

from swagger_server.models.pharmacie_add_body import PharmacieAddBody  # noqa: E501
from swagger_server.models.pharmacie_delete_body import PharmacieDeleteBody  # noqa: E501
from swagger_server.models.pharmacie_id_set_available_products_body import PharmacieIdSetAvailableProductsBody  # noqa: E501
from swagger_server.models.pharmacie_id_set_unvailable_products_body import PharmacieIdSetUnvailableProductsBody  # noqa: E501
from swagger_server.models.products_add_body import ProductsAddBody  # noqa: E501
from swagger_server.models.products_delete_body import ProductsDeleteBody  # noqa: E501
from swagger_server import util


def health_get():  # noqa: E501
    """Get server health status

     # noqa: E501


    :rtype: object
    """
    return 'do some magic!'


def pharmacie_add_post(body):  # noqa: E501
    """add a pharmacie

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: object
    """
    if connexion.request.is_json:
        body = PharmacieAddBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def pharmacie_delete_post(body):  # noqa: E501
    """delete a pharmacie by id

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: object
    """
    if connexion.request.is_json:
        body = PharmacieDeleteBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def pharmacies_list_get():  # noqa: E501
    """Returns a list of pharmacies

     # noqa: E501


    :rtype: object
    """
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


def pharmacies_mananger_pharmacie_id_set_unvailable_products_post(body, pharmacie_id):  # noqa: E501
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


def pharmacies_proximities_search_product_id_get(search_product_id, lat, long):  # noqa: E501
    """Returns a list of pharmacies order by proximity with a specic product

     # noqa: E501

    :param search_product_id: product id
    :type search_product_id: str
    :param lat: client location latitude
    :type lat: float
    :param long: client location longitude
    :type long: float

    :rtype: object
    """
    return 'do some magic!'


def products_add_post(body):  # noqa: E501
    """add a product

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: object
    """
    if connexion.request.is_json:
        body = ProductsAddBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def products_delete_post(body):  # noqa: E501
    """delete a product

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: object
    """
    if connexion.request.is_json:
        body = ProductsDeleteBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def products_list_get():  # noqa: E501
    """Returns a list of products

     # noqa: E501


    :rtype: object
    """
    return 'do some magic!'
