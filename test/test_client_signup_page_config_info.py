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

from openapi_client.models.client_signup_page_config_info import ClientSignupPageConfigInfo  # noqa: E501

class TestClientSignupPageConfigInfo(unittest.TestCase):
    """ClientSignupPageConfigInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClientSignupPageConfigInfo:
        """Test ClientSignupPageConfigInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClientSignupPageConfigInfo`
        """
        model = ClientSignupPageConfigInfo()  # noqa: E501
        if include_optional:
            return ClientSignupPageConfigInfo(
                cc_emails = [
                    ''
                    ],
                company_logo_url = '',
                company_name = '',
                landing_image_url = '',
                notification_email_subject = '',
                public_notes = '',
                signup_id = '',
                video_link = ''
            )
        else:
            return ClientSignupPageConfigInfo(
        )
        """

    def testClientSignupPageConfigInfo(self):
        """Test ClientSignupPageConfigInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
