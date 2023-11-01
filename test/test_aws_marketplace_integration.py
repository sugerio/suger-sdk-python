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

from openapi_client.models.aws_marketplace_integration import \
    AwsMarketplaceIntegration  # noqa: E501


class TestAwsMarketplaceIntegration(unittest.TestCase):
    """AwsMarketplaceIntegration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AwsMarketplaceIntegration:
        """Test AwsMarketplaceIntegration
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `AwsMarketplaceIntegration`
        """
        model = AwsMarketplaceIntegration()  # noqa: E501
        if include_optional:
            return AwsMarketplaceIntegration(
                basic_info_full_sync_done = True,
                create_entitlement_before_notification_enabled = True,
                enable_marketplace_beta_api = True,
                event_bridge_rule_name = '',
                external_id = '',
                iam_role_arn = '',
                marketplace_start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                mcas_full_sync_done = True,
                mcas_iam_role_arn = '',
                mcas_s3_bucket = '',
                mcas_sns_topic = '',
                mcas_sync_disabled = True,
                mdfs_full_sync_done = True,
                mdfs_kms_key_arn = '',
                mdfs_s3_bucket_arn = '',
                mdfs_sync_disabled = True,
                policy_arns = [
                    ''
                    ],
                revenue_record_full_sync_done = True,
                signup_redirect_without_entitlement_enabled = True,
                usage_metering_disabled = True
            )
        else:
            return AwsMarketplaceIntegration(
        )
        """

    def testAwsMarketplaceIntegration(self):
        """Test AwsMarketplaceIntegration"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
