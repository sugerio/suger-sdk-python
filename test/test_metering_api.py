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

from openapi_client.api.metering_api import MeteringApi  # noqa: E501


class TestMeteringApi(unittest.TestCase):
    """MeteringApi unit test stubs"""

    def setUp(self) -> None:
        self.api = MeteringApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_batch_report_usage_record_groups(self) -> None:
        """Test case for batch_report_usage_record_groups

        batch report usageRecordGroups  # noqa: E501
        """
        pass

    def test_batch_validate_usage_record_groups(self) -> None:
        """Test case for batch_validate_usage_record_groups

        batch validate usageRecordGroups  # noqa: E501
        """
        pass

    def test_delete_usage_record_group(self) -> None:
        """Test case for delete_usage_record_group

        delete usageRecordGroup  # noqa: E501
        """
        pass

    def test_get_usage_metering_config_info(self) -> None:
        """Test case for get_usage_metering_config_info

        get usage metering config info  # noqa: E501
        """
        pass

    def test_get_usage_record_group(self) -> None:
        """Test case for get_usage_record_group

        get usageRecordGroup  # noqa: E501
        """
        pass

    def test_get_usage_record_report(self) -> None:
        """Test case for get_usage_record_report

        get usageRecordReport  # noqa: E501
        """
        pass

    def test_list_usage_record_groups(self) -> None:
        """Test case for list_usage_record_groups

        list usageRecordGroups  # noqa: E501
        """
        pass

    def test_list_usage_record_groups_by_entitlement(self) -> None:
        """Test case for list_usage_record_groups_by_entitlement

        list usageRecordGroups by entitlement  # noqa: E501
        """
        pass

    def test_list_usage_record_groups_by_product(self) -> None:
        """Test case for list_usage_record_groups_by_product

        list usageRecordGroups by product  # noqa: E501
        """
        pass

    def test_list_usage_record_reports(self) -> None:
        """Test case for list_usage_record_reports

        list usageRecordReports  # noqa: E501
        """
        pass

    def test_report_usage_record_group(self) -> None:
        """Test case for report_usage_record_group

        report usageRecordGroup  # noqa: E501
        """
        pass

    def test_update_usage_metering_config_info(self) -> None:
        """Test case for update_usage_metering_config_info

        update usage metering config info  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
