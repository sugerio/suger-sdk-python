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

from openapi_client.models.list_notification_messages_response import (
    ListNotificationMessagesResponse,
)  # noqa: E501


class TestListNotificationMessagesResponse(unittest.TestCase):
    """ListNotificationMessagesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListNotificationMessagesResponse:
        """Test ListNotificationMessagesResponse
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ListNotificationMessagesResponse`
        """
        model = ListNotificationMessagesResponse()  # noqa: E501
        if include_optional:
            return ListNotificationMessagesResponse(
                next_offset = 56,
                notification_messages = [
                    openapi_client.models.notification_message.NotificationMessage(
                        creation_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        id = '', 
                        info = openapi_client.models.notification_message_info.NotificationMessageInfo(
                            cc_recipients = [
                                ''
                                ], 
                            custom_fields = {
                                'key' : ''
                                }, 
                            html_content = '', 
                            rcc_recipients = [
                                ''
                                ], 
                            subject = '', 
                            text_content = '', ), 
                        organization_id = '', 
                        recipient = '', 
                        type = 'Email', )
                    ],
                total_count = 56
            )
        else:
            return ListNotificationMessagesResponse(
        )
        """

    def testListNotificationMessagesResponse(self):
        """Test ListNotificationMessagesResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
