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

from suger_sdk_python.models.aws_marketplace_pre_existing_agreement import AwsMarketplacePreExistingAgreement

class TestAwsMarketplacePreExistingAgreement(unittest.TestCase):
    """AwsMarketplacePreExistingAgreement unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AwsMarketplacePreExistingAgreement:
        """Test AwsMarketplacePreExistingAgreement
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AwsMarketplacePreExistingAgreement`
        """
        model = AwsMarketplacePreExistingAgreement()
        if include_optional:
            return AwsMarketplacePreExistingAgreement(
                acquisition_channel = '',
                pricing_model = 'Contract'
            )
        else:
            return AwsMarketplacePreExistingAgreement(
        )
        """

    def testAwsMarketplacePreExistingAgreement(self):
        """Test AwsMarketplacePreExistingAgreement"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
