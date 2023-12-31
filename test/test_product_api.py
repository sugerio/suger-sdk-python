# coding: utf-8

"""
    Suger API

    CRUD operations on a set of resources, including organizations, products, offers, entitlements, usage record groups for meterting, etc.

    The version of the OpenAPI document: 1.0
    Contact: support@suger.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.product_api import ProductApi  # noqa: E501


class TestProductApi(unittest.TestCase):
    """ProductApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ProductApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_create_or_update_draft_product(self) -> None:
        """Test case for create_or_update_draft_product

        create or update draft product  # noqa: E501
        """
        pass

    def test_create_product(self) -> None:
        """Test case for create_product

        create product  # noqa: E501
        """
        pass

    def test_delete_product(self) -> None:
        """Test case for delete_product

        delete product  # noqa: E501
        """
        pass

    def test_get_product(self) -> None:
        """Test case for get_product

        get product  # noqa: E501
        """
        pass

    def test_list_product_metering_dimensions(self) -> None:
        """Test case for list_product_metering_dimensions

        list metering dimensions of product  # noqa: E501
        """
        pass

    def test_list_products_by_organization(self) -> None:
        """Test case for list_products_by_organization

        list products by organization  # noqa: E501
        """
        pass

    def test_list_products_by_partner(self) -> None:
        """Test case for list_products_by_partner

        list products by partner  # noqa: E501
        """
        pass

    def test_update_product(self) -> None:
        """Test case for update_product

        update product  # noqa: E501
        """
        pass

    def test_update_product_meta_info(self) -> None:
        """Test case for update_product_meta_info

        update product meta info  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
