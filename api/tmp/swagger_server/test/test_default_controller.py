# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.pharmacie_add_body import PharmacieAddBody  # noqa: E501
from swagger_server.models.pharmacie_delete_body import PharmacieDeleteBody  # noqa: E501
from swagger_server.models.pharmacie_id_set_available_products_body import PharmacieIdSetAvailableProductsBody  # noqa: E501
from swagger_server.models.pharmacie_id_set_unvailable_products_body import PharmacieIdSetUnvailableProductsBody  # noqa: E501
from swagger_server.models.products_add_body import ProductsAddBody  # noqa: E501
from swagger_server.models.products_delete_body import ProductsDeleteBody  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_health_get(self):
        """Test case for health_get

        Get server health status
        """
        response = self.client.open(
            '/health',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_pharmacie_add_post(self):
        """Test case for pharmacie_add_post

        add a pharmacie
        """
        body = PharmacieAddBody()
        response = self.client.open(
            '/pharmacie/add',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_pharmacie_delete_post(self):
        """Test case for pharmacie_delete_post

        delete a pharmacie by id
        """
        body = PharmacieDeleteBody()
        response = self.client.open(
            '/pharmacie/delete',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_pharmacies_list_get(self):
        """Test case for pharmacies_list_get

        Returns a list of pharmacies
        """
        response = self.client.open(
            '/pharmacies/list',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_pharmacies_mananger_pharmacie_id_set_available_products_post(self):
        """Test case for pharmacies_mananger_pharmacie_id_set_available_products_post

        set products list as available products for a pharmacie
        """
        body = PharmacieIdSetAvailableProductsBody()
        response = self.client.open(
            '/pharmacies/mananger/{pharmacie_id}/set_available_products'.format(pharmacie_id='pharmacie_id_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_pharmacies_mananger_pharmacie_id_set_unvailable_products_post(self):
        """Test case for pharmacies_mananger_pharmacie_id_set_unvailable_products_post

        set products list as available products for a pharmacie
        """
        body = PharmacieIdSetUnvailableProductsBody()
        response = self.client.open(
            '/pharmacies/mananger/{pharmacie_id}/set_unvailable_products'.format(pharmacie_id='pharmacie_id_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_pharmacies_proximities_list_get(self):
        """Test case for pharmacies_proximities_list_get

        Returns a list of pharmacies order by proximity
        """
        query_string = [('lat', 1.2),
                        ('long', 1.2)]
        response = self.client.open(
            '/pharmacies/proximities/list',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_pharmacies_proximities_search_product_id_get(self):
        """Test case for pharmacies_proximities_search_product_id_get

        Returns a list of pharmacies order by proximity with a specic product
        """
        query_string = [('lat', 1.2),
                        ('long', 1.2)]
        response = self.client.open(
            '/pharmacies/proximities/{search_product_id}'.format(search_product_id='search_product_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_products_add_post(self):
        """Test case for products_add_post

        add a product
        """
        body = ProductsAddBody()
        response = self.client.open(
            '/products/add',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_products_delete_post(self):
        """Test case for products_delete_post

        delete a product
        """
        body = ProductsDeleteBody()
        response = self.client.open(
            '/products/delete',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_products_list_get(self):
        """Test case for products_list_get

        Returns a list of products
        """
        response = self.client.open(
            '/products/list',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
