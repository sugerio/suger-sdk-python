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

from suger_sdk_python.api.support_api import SupportApi


class TestSupportApi(unittest.TestCase):
    """SupportApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SupportApi()

    def tearDown(self) -> None:
        pass

    def test_close_support_ticket(self) -> None:
        """Test case for close_support_ticket

        close support ticket
        """
        pass

    def test_create_support_ticket(self) -> None:
        """Test case for create_support_ticket

        create support ticket
        """
        pass

    def test_create_support_ticket_attachment(self) -> None:
        """Test case for create_support_ticket_attachment

        create support ticket attachment
        """
        pass

    def test_create_support_ticket_comment(self) -> None:
        """Test case for create_support_ticket_comment

        create support ticket comment
        """
        pass

    def test_get_support_ticket(self) -> None:
        """Test case for get_support_ticket

        get support ticket
        """
        pass

    def test_list_support_tickets(self) -> None:
        """Test case for list_support_tickets

        list support tickets
        """
        pass

    def test_reopen_support_ticket(self) -> None:
        """Test case for reopen_support_ticket

        reopen support ticket
        """
        pass

    def test_update_support_ticket(self) -> None:
        """Test case for update_support_ticket

        update support ticket
        """
        pass


if __name__ == '__main__':
    unittest.main()
