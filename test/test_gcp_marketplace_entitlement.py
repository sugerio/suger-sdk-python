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

from suger_sdk_python.models.gcp_marketplace_entitlement import GcpMarketplaceEntitlement

class TestGcpMarketplaceEntitlement(unittest.TestCase):
    """GcpMarketplaceEntitlement unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GcpMarketplaceEntitlement:
        """Test GcpMarketplaceEntitlement
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GcpMarketplaceEntitlement`
        """
        model = GcpMarketplaceEntitlement()
        if include_optional:
            return GcpMarketplaceEntitlement(
                account = '',
                consumers = [
                    {"project":"project"}
                    ],
                create_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = '',
                input_properties = [
                    56
                    ],
                message_to_user = '',
                name = '',
                new_offer_duration = '',
                new_offer_end_time = '',
                new_offer_start_time = '',
                new_pending_offer = '',
                new_pending_offer_duration = '',
                new_pending_plan = '',
                new_plan = '',
                offer = '',
                offer_duration = '',
                offer_effective_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                offer_end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                plan = '',
                product = '',
                product_external_name = '',
                provider = '',
                quote_external_name = '',
                state = 'ENTITLEMENT_STATE_UNSPECIFIED',
                subscription_end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                usage_reporting_id = ''
            )
        else:
            return GcpMarketplaceEntitlement(
        )
        """

    def testGcpMarketplaceEntitlement(self):
        """Test GcpMarketplaceEntitlement"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
