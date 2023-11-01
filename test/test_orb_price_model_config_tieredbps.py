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

from openapi_client.models.orb_price_model_config_tieredbps import \
    OrbPriceModelConfigTIEREDBPS  # noqa: E501


class TestOrbPriceModelConfigTIEREDBPS(unittest.TestCase):
    """OrbPriceModelConfigTIEREDBPS unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OrbPriceModelConfigTIEREDBPS:
        """Test OrbPriceModelConfigTIEREDBPS
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `OrbPriceModelConfigTIEREDBPS`
        """
        model = OrbPriceModelConfigTIEREDBPS()  # noqa: E501
        if include_optional:
            return OrbPriceModelConfigTIEREDBPS(
                tiers = [
                    openapi_client.models.orb_price_tier.OrbPriceTier(
                        bps = 1.337, 
                        first_unit = '', 
                        last_unit = '', 
                        maximum_amount = '', 
                        maximum_units = 1.337, 
                        minimum_amount = '', 
                        per_unit_maximum = '', 
                        unit_amount = '', )
                    ]
            )
        else:
            return OrbPriceModelConfigTIEREDBPS(
        )
        """

    def testOrbPriceModelConfigTIEREDBPS(self):
        """Test OrbPriceModelConfigTIEREDBPS"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
