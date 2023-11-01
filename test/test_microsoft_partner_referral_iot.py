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
import datetime

from openapi_client.models.microsoft_partner_referral_iot import (
    MicrosoftPartnerReferralIot,
)  # noqa: E501


class TestMicrosoftPartnerReferralIot(unittest.TestCase):
    """MicrosoftPartnerReferralIot unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MicrosoftPartnerReferralIot:
        """Test MicrosoftPartnerReferralIot
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `MicrosoftPartnerReferralIot`
        """
        model = MicrosoftPartnerReferralIot()  # noqa: E501
        if include_optional:
            return MicrosoftPartnerReferralIot(
                attach_services = True,
                azure_certified_device = True,
                customer_license_agreement_number = openapi_client.models.customer_license_agreement_number.customerLicenseAgreementNumber(),
                device_category = openapi_client.models.device_category.deviceCategory(),
                silicon_type = openapi_client.models.silicon_type.siliconType()
            )
        else:
            return MicrosoftPartnerReferralIot(
        )
        """

    def testMicrosoftPartnerReferralIot(self):
        """Test MicrosoftPartnerReferralIot"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
