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

from suger_sdk_python.api.billing_api import BillingApi


class TestBillingApi(unittest.TestCase):
    """BillingApi unit test stubs"""

    def setUp(self) -> None:
        self.api = BillingApi()

    def tearDown(self) -> None:
        pass

    def test_create_addon(self) -> None:
        """Test case for create_addon

        create addon
        """
        pass

    def test_create_refund(self) -> None:
        """Test case for create_refund

        create refund.
        """
        pass

    def test_delete_addon(self) -> None:
        """Test case for delete_addon

        delete addon
        """
        pass

    def test_get_addon(self) -> None:
        """Test case for get_addon

        get addon
        """
        pass

    def test_get_invoice_v2(self) -> None:
        """Test case for get_invoice_v2

        get invoice
        """
        pass

    def test_issue_invoice_v2(self) -> None:
        """Test case for issue_invoice_v2

        issue invoice
        """
        pass

    def test_list_addons(self) -> None:
        """Test case for list_addons

        list addons
        """
        pass

    def test_list_invoices(self) -> None:
        """Test case for list_invoices

        list invoices
        """
        pass

    def test_list_payment_transactions(self) -> None:
        """Test case for list_payment_transactions

        list payment transactions
        """
        pass

    def test_list_refund_of_payment_transaction(self) -> None:
        """Test case for list_refund_of_payment_transaction

        list refunds.
        """
        pass

    def test_pay_invoice_v2(self) -> None:
        """Test case for pay_invoice_v2

        pay invoice
        """
        pass

    def test_preview_invoice_email(self) -> None:
        """Test case for preview_invoice_email

        preview invoice email
        """
        pass

    def test_update_addon(self) -> None:
        """Test case for update_addon

        update addon
        """
        pass

    def test_update_invoice_info_v2(self) -> None:
        """Test case for update_invoice_info_v2

        update invoice info
        """
        pass

    def test_void_invoice_v2(self) -> None:
        """Test case for void_invoice_v2

        void invoice
        """
        pass


if __name__ == '__main__':
    unittest.main()
