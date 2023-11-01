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

from openapi_client.models.slack_o_auth_v2_response_enterprise import (
    SlackOAuthV2ResponseEnterprise,
)  # noqa: E501


class TestSlackOAuthV2ResponseEnterprise(unittest.TestCase):
    """SlackOAuthV2ResponseEnterprise unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SlackOAuthV2ResponseEnterprise:
        """Test SlackOAuthV2ResponseEnterprise
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `SlackOAuthV2ResponseEnterprise`
        """
        model = SlackOAuthV2ResponseEnterprise()  # noqa: E501
        if include_optional:
            return SlackOAuthV2ResponseEnterprise(
                id = '',
                name = ''
            )
        else:
            return SlackOAuthV2ResponseEnterprise(
        )
        """

    def testSlackOAuthV2ResponseEnterprise(self):
        """Test SlackOAuthV2ResponseEnterprise"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()