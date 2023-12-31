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

from openapi_client.models.orb_price_model_config_package import OrbPriceModelConfigPACKAGE  # noqa: E501

class TestOrbPriceModelConfigPACKAGE(unittest.TestCase):
    """OrbPriceModelConfigPACKAGE unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrbPriceModelConfigPACKAGE:
        """Test OrbPriceModelConfigPACKAGE
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OrbPriceModelConfigPACKAGE`
        """
        model = OrbPriceModelConfigPACKAGE()  # noqa: E501
        if include_optional:
            return OrbPriceModelConfigPACKAGE(
                package_amount = '',
                package_size = 1.337
            )
        else:
            return OrbPriceModelConfigPACKAGE(
        )
        """

    def testOrbPriceModelConfigPACKAGE(self):
        """Test OrbPriceModelConfigPACKAGE"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
