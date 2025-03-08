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

from suger_sdk_python.models.azure_product_variant_custom_meter import AzureProductVariantCustomMeter

class TestAzureProductVariantCustomMeter(unittest.TestCase):
    """AzureProductVariantCustomMeter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AzureProductVariantCustomMeter:
        """Test AzureProductVariantCustomMeter
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AzureProductVariantCustomMeter`
        """
        model = AzureProductVariantCustomMeter()
        if include_optional:
            return AzureProductVariantCustomMeter(
                display_name = '',
                id = '',
                included_base_quantities = [
                    {"quantity":7.386281948385884,"isInfinite":true,"recurringUnit":"Monthly"}
                    ],
                is_enabled = True,
                price_in_usd = 1.337,
                unique_id = '',
                unit_of_measure = ''
            )
        else:
            return AzureProductVariantCustomMeter(
        )
        """

    def testAzureProductVariantCustomMeter(self):
        """Test AzureProductVariantCustomMeter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
