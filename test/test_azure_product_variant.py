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

from suger_sdk_python.models.azure_product_variant import AzureProductVariant

class TestAzureProductVariant(unittest.TestCase):
    """AzureProductVariant unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AzureProductVariant:
        """Test AzureProductVariant
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AzureProductVariant`
        """
        model = AzureProductVariant()
        if include_optional:
            return AzureProductVariant(
                azure_government_certifications = [
                    {"validationResults":[{"errorMessage":"errorMessage","memberNames":["memberNames","memberNames"]},{"errorMessage":"errorMessage","memberNames":["memberNames","memberNames"]}],"title":"title","uri":"uri"}
                    ],
                cloud_availabilities = [
                    ''
                    ],
                conversion_paths = '',
                extended_properties = [
                    {"type":"type","value":"value"}
                    ],
                external_id = '',
                feature_availabilities = [
                    {"markets":[{"marketCode":"marketCode","friendlyName":"friendlyName"},{"marketCode":"marketCode","friendlyName":"friendlyName"}],"visibility":"Public","priceSchedules":[{"isBaseSchedule":true,"schedules":[{"pricingModel":"Flat","pricingUnits":[{"unitType":"unitType","name":"sharedcore","lowerUnit":9,"upperUnit":6,"isUnlimitedUnit":true},{"unitType":"unitType","name":"sharedcore","lowerUnit":9,"upperUnit":6,"isUnlimitedUnit":true}],"priceCadence":{"type":"Month","value":9},"retailPrice":{"openPrice":8.762042012749001,"priceTierID":"priceTierID","currencyCode":"currencyCode"}},{"pricingModel":"Flat","pricingUnits":[{"unitType":"unitType","name":"sharedcore","lowerUnit":9,"upperUnit":6,"isUnlimitedUnit":true},{"unitType":"unitType","name":"sharedcore","lowerUnit":9,"upperUnit":6,"isUnlimitedUnit":true}],"priceCadence":{"type":"Month","value":9},"retailPrice":{"openPrice":8.762042012749001,"priceTierID":"priceTierID","currencyCode":"currencyCode"}}],"dateTimeRange":{"endAt":{"dateTimeInUtc":"dateTimeInUtc","localizePerMarket":true},"startAt":{"dateTimeInUtc":"dateTimeInUtc","localizePerMarket":true}},"marketCodes":["marketCodes","marketCodes"],"friendlyName":"friendlyName"},{"isBaseSchedule":true,"schedules":[{"pricingModel":"Flat","pricingUnits":[{"unitType":"unitType","name":"sharedcore","lowerUnit":9,"upperUnit":6,"isUnlimitedUnit":true},{"unitType":"unitType","name":"sharedcore","lowerUnit":9,"upperUnit":6,"isUnlimitedUnit":true}],"priceCadence":{"type":"Month","value":9},"retailPrice":{"openPrice":8.762042012749001,"priceTierID":"priceTierID","currencyCode":"currencyCode"}},{"pricingModel":"Flat","pricingUnits":[{"unitType":"unitType","name":"sharedcore","lowerUnit":9,"upperUnit":6,"isUnlimitedUnit":true},{"unitType":"unitType","name":"sharedcore","lowerUnit":9,"upperUnit":6,"isUnlimitedUnit":true}],"priceCadence":{"type":"Month","value":9},"retailPrice":{"openPrice":8.762042012749001,"priceTierID":"priceTierID","currencyCode":"currencyCode"}}],"dateTimeRange":{"endAt":{"dateTimeInUtc":"dateTimeInUtc","localizePerMarket":true},"startAt":{"dateTimeInUtc":"dateTimeInUtc","localizePerMarket":true}},"marketCodes":["marketCodes","marketCodes"],"friendlyName":"friendlyName"}],"customMeters":[{"unitOfMeasure":"unitOfMeasure","displayName":"displayName","includedBaseQuantities":[{"quantity":7.386281948385884,"isInfinite":true,"recurringUnit":"Monthly"},{"quantity":7.386281948385884,"isInfinite":true,"recurringUnit":"Monthly"}],"isEnabled":true,"priceInUsd":5.025004791520295,"id":"id","uniqueID":"uniqueID"},{"unitOfMeasure":"unitOfMeasure","displayName":"displayName","includedBaseQuantities":[{"quantity":7.386281948385884,"isInfinite":true,"recurringUnit":"Monthly"},{"quantity":7.386281948385884,"isInfinite":true,"recurringUnit":"Monthly"}],"isEnabled":true,"priceInUsd":5.025004791520295,"id":"id","uniqueID":"uniqueID"}],"marketStates":[{"marketCode":"marketCode","state":"Disabled"},{"marketCode":"marketCode","state":"Disabled"}],"tenantAudiences":[{"description":"description","id":"id"},{"description":"description","id":"id"}],"subscriptionAudiences":[{"description":"description","id":"id"},{"description":"description","id":"id"}],"id":"id","properties":[{"type":"type","value":"value"},{"type":"type","value":"value"}],"trial":{"duration":9,"dateTimeRange":{"endAt":{"dateTimeInUtc":"dateTimeInUtc","localizePerMarket":true},"startAt":{"dateTimeInUtc":"dateTimeInUtc","localizePerMarket":true}},"type":"NoTrial","durationType":"Minute"},"isHidden":true,"resourceType":"resourceType"}
                    ],
                friendly_name = '',
                id = '',
                lead_gen_id = '',
                reference_variant_id = '',
                resource_type = 'AzureSkuVariant',
                state = 'InActive'
            )
        else:
            return AzureProductVariant(
        )
        """

    def testAzureProductVariant(self):
        """Test AzureProductVariant"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
