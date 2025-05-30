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

from suger_sdk_python.models.gcp_marketplace_product_service_config import GcpMarketplaceProductServiceConfig

class TestGcpMarketplaceProductServiceConfig(unittest.TestCase):
    """GcpMarketplaceProductServiceConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GcpMarketplaceProductServiceConfig:
        """Test GcpMarketplaceProductServiceConfig
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GcpMarketplaceProductServiceConfig`
        """
        model = GcpMarketplaceProductServiceConfig()
        if include_optional:
            return GcpMarketplaceProductServiceConfig(
                billing = {"metrics":["metrics","metrics"]},
                metrics = [
                    {"priceTiers":[{"startingUsageAmount":"startingUsageAmount","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"},"fromAmount":1.2315135367772556},{"startingUsageAmount":"startingUsageAmount","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"},"fromAmount":1.2315135367772556}],"displayUnitDescription":"displayUnitDescription","unit":"unit","metricKind":"metricKind","displayName":"displayName","valueType":"{}","name":"name","description":"description","displayUnit":"displayUnit","id":"id","reportingUnit":"reportingUnit","skuId":"skuId"}
                    ],
                name = '',
                producer_project_id = '',
                title = ''
            )
        else:
            return GcpMarketplaceProductServiceConfig(
        )
        """

    def testGcpMarketplaceProductServiceConfig(self):
        """Test GcpMarketplaceProductServiceConfig"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
