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

from suger_sdk_python.models.gcp_marketplace_product import GcpMarketplaceProduct

class TestGcpMarketplaceProduct(unittest.TestCase):
    """GcpMarketplaceProduct unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GcpMarketplaceProduct:
        """Test GcpMarketplaceProduct
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GcpMarketplaceProduct`
        """
        model = GcpMarketplaceProduct()
        if include_optional:
            return GcpMarketplaceProduct(
                create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                derived_discovery_state = {"accessState":"ALLUSERS_ACCESSIBLE","searchState":"ADMIN_OVERRIDE_UNSEARCHABLE"},
                id = '',
                last_publish_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                listing_spec = {"marketingSpec":{"signupUri":"signupUri","externalLicenseSpecs":[{"description":"description","uri":"uri"},{"description":"description","uri":"uri"}],"searchKeywords":["searchKeywords","searchKeywords"],"tagLine":"tagLine","displayNames":["displayNames","displayNames"],"externalMarketingUrl":"externalMarketingUrl","icon":"icon","description":"description","searchCategories":["searchCategories","searchCategories"],"searchDescription":"searchDescription","title":"title","supportSpec":{"description":"description","uri":"uri","email":"email"},"eulaUrl":"eulaUrl","documentationSpecs":[{"description":"description","title":"title","uri":"uri"},{"description":"description","title":"title","uri":"uri"}]},"purchaseSpec":{"features":[{"name":"name","description":"description","title":"title"},{"name":"name","description":"description","title":"title"}],"purchaseOptionSpecs":[{"priceInfo":{"usageFees":[{"priceTiers":[{"startingUsageAmount":"startingUsageAmount","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"},"fromAmount":7.386281948385884},{"startingUsageAmount":"startingUsageAmount","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"},"fromAmount":7.386281948385884}],"metricId":"metricId","displayQuantity":7},{"priceTiers":[{"startingUsageAmount":"startingUsageAmount","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"},"fromAmount":7.386281948385884},{"startingUsageAmount":"startingUsageAmount","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"},"fromAmount":7.386281948385884}],"metricId":"metricId","displayQuantity":7}],"subscriptionPlans":[{"period":"period","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"}},{"period":"period","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"}}],"description":"description","priceModel":"FREE"},"purchaseMode":"PURCHASE_MODE_PRIVATE","name":"name","title":"title","featureValues":[{"featureValue":"featureValue","featureTitle":"featureTitle","featureName":"featureName","featureDescription":"featureDescription"},{"featureValue":"featureValue","featureTitle":"featureTitle","featureName":"featureName","featureDescription":"featureDescription"}]},{"priceInfo":{"usageFees":[{"priceTiers":[{"startingUsageAmount":"startingUsageAmount","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"},"fromAmount":7.386281948385884},{"startingUsageAmount":"startingUsageAmount","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"},"fromAmount":7.386281948385884}],"metricId":"metricId","displayQuantity":7},{"priceTiers":[{"startingUsageAmount":"startingUsageAmount","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"},"fromAmount":7.386281948385884},{"startingUsageAmount":"startingUsageAmount","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"},"fromAmount":7.386281948385884}],"metricId":"metricId","displayQuantity":7}],"subscriptionPlans":[{"period":"period","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"}},{"period":"period","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"}}],"description":"description","priceModel":"FREE"},"purchaseMode":"PURCHASE_MODE_PRIVATE","name":"name","title":"title","featureValues":[{"featureValue":"featureValue","featureTitle":"featureTitle","featureName":"featureName","featureDescription":"featureDescription"},{"featureValue":"featureValue","featureTitle":"featureTitle","featureName":"featureName","featureDescription":"featureDescription"}]}],"metrics":[{"priceTiers":[{"startingUsageAmount":"startingUsageAmount","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"},"fromAmount":7.386281948385884},{"startingUsageAmount":"startingUsageAmount","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"},"fromAmount":7.386281948385884}],"displayUnitDescription":"displayUnitDescription","unit":"unit","metricKind":"metricKind","displayName":"displayName","valueType":"{}","name":"name","description":"description","displayUnit":"displayUnit","id":"id","reportingUnit":"reportingUnit","skuId":"skuId"},{"priceTiers":[{"startingUsageAmount":"startingUsageAmount","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"},"fromAmount":7.386281948385884},{"startingUsageAmount":"startingUsageAmount","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"},"fromAmount":7.386281948385884}],"displayUnitDescription":"displayUnitDescription","unit":"unit","metricKind":"metricKind","displayName":"displayName","valueType":"{}","name":"name","description":"description","displayUnit":"displayUnit","id":"id","reportingUnit":"reportingUnit","skuId":"skuId"}]},"listingType":"BillingIntegratedManagedService","termsSpec":{"standardEula":"{}","inlineEula":"{}","eulaUri":"eulaUri"},"externalAccountSpec":{"signupUri":"signupUri","loginUri":"loginUri","singleSignOnUri":"singleSignOnUri"}},
                marketplace = 'marketplaces/google-cloud',
                name = '',
                revision_create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                revision_id = '',
                service = '',
                service_config = {"name":"name","producerProjectId":"producerProjectId","metrics":[{"priceTiers":[{"startingUsageAmount":"startingUsageAmount","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"},"fromAmount":7.386281948385884},{"startingUsageAmount":"startingUsageAmount","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"},"fromAmount":7.386281948385884}],"displayUnitDescription":"displayUnitDescription","unit":"unit","metricKind":"metricKind","displayName":"displayName","valueType":"{}","name":"name","description":"description","displayUnit":"displayUnit","id":"id","reportingUnit":"reportingUnit","skuId":"skuId"},{"priceTiers":[{"startingUsageAmount":"startingUsageAmount","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"},"fromAmount":7.386281948385884},{"startingUsageAmount":"startingUsageAmount","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"},"fromAmount":7.386281948385884}],"displayUnitDescription":"displayUnitDescription","unit":"unit","metricKind":"metricKind","displayName":"displayName","valueType":"{}","name":"name","description":"description","displayUnit":"displayUnit","id":"id","reportingUnit":"reportingUnit","skuId":"skuId"}],"title":"title","billing":{"metrics":["metrics","metrics"]}},
                validation_summary = None
            )
        else:
            return GcpMarketplaceProduct(
        )
        """

    def testGcpMarketplaceProduct(self):
        """Test GcpMarketplaceProduct"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
