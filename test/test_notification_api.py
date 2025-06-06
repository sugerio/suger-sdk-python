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

from suger_sdk_python.api.notification_api import NotificationApi


class TestNotificationApi(unittest.TestCase):
    """NotificationApi unit test stubs"""

    def setUp(self) -> None:
        self.api = NotificationApi()

    def tearDown(self) -> None:
        pass

    def test_get_notification_message(self) -> None:
        """Test case for get_notification_message

        get notification message
        """
        pass

    def test_list_notification_events(self) -> None:
        """Test case for list_notification_events

        list notification events
        """
        pass

    def test_list_notification_events_by_entity(self) -> None:
        """Test case for list_notification_events_by_entity

        list notification events by entity
        """
        pass

    def test_list_notification_messages(self) -> None:
        """Test case for list_notification_messages

        list notification messages
        """
        pass


if __name__ == '__main__':
    unittest.main()
