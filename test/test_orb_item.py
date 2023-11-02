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
import datetime

from openapi_client.models.orb_item import OrbItem  # noqa: E501

class TestOrbItem(unittest.TestCase):
    """OrbItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrbItem:
        """Test OrbItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrbItem`
        """
        model = OrbItem()  # noqa: E501
        if include_optional:
            return OrbItem(
                created_at = '',
                external_connections = [
                    openapi_client.models.orb_external_connection.OrbExternalConnection(
                        external_connection_name = 'stripe', 
                        external_entity_id = '', )
                    ],
                id = '',
                name = ''
            )
        else:
            return OrbItem(
        )
        """

    def testOrbItem(self):
        """Test OrbItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
