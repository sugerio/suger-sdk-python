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

from openapi_client.models.microsoft_partner_referral_tracking_info import \
    MicrosoftPartnerReferralTrackingInfo  # noqa: E501


class TestMicrosoftPartnerReferralTrackingInfo(unittest.TestCase):
    """MicrosoftPartnerReferralTrackingInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MicrosoftPartnerReferralTrackingInfo:
        """Test MicrosoftPartnerReferralTrackingInfo
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `MicrosoftPartnerReferralTrackingInfo`
        """
        model = MicrosoftPartnerReferralTrackingInfo()  # noqa: E501
        if include_optional:
            return MicrosoftPartnerReferralTrackingInfo(
                microsoft_msx_id = openapi_client.models.microsoft_msx_id.microsoftMsxId(),
                microsoft_us_fed_lead_id = openapi_client.models.microsoft_us_fed_lead_id.microsoftUSFedLeadId(),
                microsoft_us_fedopportunity_id = openapi_client.models.microsoft_us_fedopportunity_id.microsoftUSFedopportunityId(),
                migrated_psc_deal_id = openapi_client.models.migrated_psc_deal_id.migratedPSCDealId(),
                migrated_psc_partner_deal_id = openapi_client.models.migrated_psc_partner_deal_id.migratedPSCPartnerDealId()
            )
        else:
            return MicrosoftPartnerReferralTrackingInfo(
        )
        """

    def testMicrosoftPartnerReferralTrackingInfo(self):
        """Test MicrosoftPartnerReferralTrackingInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
