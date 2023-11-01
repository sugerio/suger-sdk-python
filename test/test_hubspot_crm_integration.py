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

from openapi_client.models.hubspot_crm_integration import \
    HubspotCrmIntegration  # noqa: E501


class TestHubspotCrmIntegration(unittest.TestCase):
    """HubspotCrmIntegration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HubspotCrmIntegration:
        """Test HubspotCrmIntegration
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `HubspotCrmIntegration`
        """
        model = HubspotCrmIntegration()  # noqa: E501
        if include_optional:
            return HubspotCrmIntegration(
                company_fields = [
                    ''
                    ],
                contact_fields = [
                    ''
                    ],
                credential = openapi_client.models.hubspot_crm_credential.HubspotCrmCredential(
                    access_token = '', 
                    acquired_on = 56, 
                    expires_in = 56, 
                    refresh_token = '', ),
                deal_fields = [
                    ''
                    ],
                paused = True,
                portal_id = 56,
                secret_key = '',
                sync_filters = [
                    openapi_client.models.hubspot_sync_filter.HubspotSyncFilter(
                        operator = '', 
                        property_name = '', 
                        value = '', )
                    ]
            )
        else:
            return HubspotCrmIntegration(
        )
        """

    def testHubspotCrmIntegration(self):
        """Test HubspotCrmIntegration"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
