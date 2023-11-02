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

from openapi_client.models.slack_integration import SlackIntegration  # noqa: E501

class TestSlackIntegration(unittest.TestCase):
    """SlackIntegration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SlackIntegration:
        """Test SlackIntegration
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SlackIntegration`
        """
        model = SlackIntegration()  # noqa: E501
        if include_optional:
            return SlackIntegration(
                access_token = '',
                app_id = '',
                authed_user = openapi_client.models.slack/o_auth_v2_response_authed_user.slack.OAuthV2ResponseAuthedUser(
                    access_token = '', 
                    expires_in = 56, 
                    id = '', 
                    refresh_token = '', 
                    scope = '', 
                    token_type = '', ),
                bot_user_id = '',
                enterprise = openapi_client.models.slack/o_auth_v2_response_enterprise.slack.OAuthV2ResponseEnterprise(
                    id = '', 
                    name = '', ),
                expires_in = 56,
                incoming_webhook = openapi_client.models.slack/o_auth_response_incoming_webhook.slack.OAuthResponseIncomingWebhook(
                    channel = '', 
                    channel_id = '', 
                    configuration_url = '', 
                    url = '', ),
                redirect_url = '',
                refresh_token = '',
                scope = '',
                team = openapi_client.models.slack/o_auth_v2_response_team.slack.OAuthV2ResponseTeam(
                    id = '', 
                    name = '', ),
                token_type = ''
            )
        else:
            return SlackIntegration(
        )
        """

    def testSlackIntegration(self):
        """Test SlackIntegration"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
