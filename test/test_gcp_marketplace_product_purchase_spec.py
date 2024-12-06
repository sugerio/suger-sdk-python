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

from suger_sdk_python.models.gcp_marketplace_product_purchase_spec import GcpMarketplaceProductPurchaseSpec

class TestGcpMarketplaceProductPurchaseSpec(unittest.TestCase):
    """GcpMarketplaceProductPurchaseSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GcpMarketplaceProductPurchaseSpec:
        """Test GcpMarketplaceProductPurchaseSpec
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GcpMarketplaceProductPurchaseSpec`
        """
        model = GcpMarketplaceProductPurchaseSpec()
        if include_optional:
            return GcpMarketplaceProductPurchaseSpec(
                features = [
                    {"name":"name","description":"description","title":"title"}
                    ],
                metrics = [
                    {"priceTiers":[{"startingUsageAmount":"startingUsageAmount","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"},"fromAmount":7.386281948385884},{"startingUsageAmount":"startingUsageAmount","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"},"fromAmount":7.386281948385884}],"displayUnitDescription":"displayUnitDescription","unit":"unit","metricKind":"metricKind","displayName":"displayName","valueType":"{}","name":"name","description":"description","displayUnit":"displayUnit","id":"id","reportingUnit":"reportingUnit","skuId":"skuId"}
                    ],
                purchase_option_specs = [
                    {"priceInfo":{"usageFees":[{"priceTiers":[{"startingUsageAmount":"startingUsageAmount","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"},"fromAmount":7.386281948385884},{"startingUsageAmount":"startingUsageAmount","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"},"fromAmount":7.386281948385884}],"metricId":"metricId","displayQuantity":7},{"priceTiers":[{"startingUsageAmount":"startingUsageAmount","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"},"fromAmount":7.386281948385884},{"startingUsageAmount":"startingUsageAmount","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"},"fromAmount":7.386281948385884}],"metricId":"metricId","displayQuantity":7}],"subscriptionPlans":[{"period":"period","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"}},{"period":"period","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"}}],"description":"description","priceModel":"FREE"},"purchaseMode":"PURCHASE_MODE_PRIVATE","name":"name","title":"title","featureValues":[{"featureValue":"featureValue","featureTitle":"featureTitle","featureName":"featureName","featureDescription":"featureDescription"},{"featureValue":"featureValue","featureTitle":"featureTitle","featureName":"featureName","featureDescription":"featureDescription"}]}
                    ]
            )
        else:
            return GcpMarketplaceProductPurchaseSpec(
        )
        """

    def testGcpMarketplaceProductPurchaseSpec(self):
        """Test GcpMarketplaceProductPurchaseSpec"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
