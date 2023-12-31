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

from openapi_client.models.slack_o_auth_v2_response_authed_user import SlackOAuthV2ResponseAuthedUser  # noqa: E501

class TestSlackOAuthV2ResponseAuthedUser(unittest.TestCase):
    """SlackOAuthV2ResponseAuthedUser unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SlackOAuthV2ResponseAuthedUser:
        """Test SlackOAuthV2ResponseAuthedUser
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SlackOAuthV2ResponseAuthedUser`
        """
        model = SlackOAuthV2ResponseAuthedUser()  # noqa: E501
        if include_optional:
            return SlackOAuthV2ResponseAuthedUser(
                access_token = '',
                expires_in = 56,
                id = '',
                refresh_token = '',
                scope = '',
                token_type = ''
            )
        else:
            return SlackOAuthV2ResponseAuthedUser(
        )
        """

    def testSlackOAuthV2ResponseAuthedUser(self):
        """Test SlackOAuthV2ResponseAuthedUser"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
