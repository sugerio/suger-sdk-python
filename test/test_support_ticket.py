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

from suger_sdk_python.models.support_ticket import SupportTicket

class TestSupportTicket(unittest.TestCase):
    """SupportTicket unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SupportTicket:
        """Test SupportTicket
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SupportTicket`
        """
        model = SupportTicket()
        if include_optional:
            return SupportTicket(
                attachments = [
                    {"date":"date","thumbnail_small":"thumbnail_small","thumbnail_medium":"thumbnail_medium","size":0,"thumbnail_large":"thumbnail_large","mimetype":"mimetype","id":"id","title":"title","url":"url"}
                    ],
                close_time = '',
                comments = [
                    {"date":"date","comment_text":"comment_text","creator":"{}","comment":[{"image":{"thumbnail_small":"thumbnail_small","extension":"extension","thumbnail_medium":"thumbnail_medium","thumbnail_large":"thumbnail_large","name":"name","id":"id","title":"title","type":"type","url":"url"},"attachment":{"date":"date","thumbnail_small":"thumbnail_small","thumbnail_medium":"thumbnail_medium","size":0,"thumbnail_large":"thumbnail_large","mimetype":"mimetype","id":"id","title":"title","url":"url"},"text":"text","type":"type","frame":{"id":"id","url":"url"}},{"image":{"thumbnail_small":"thumbnail_small","extension":"extension","thumbnail_medium":"thumbnail_medium","thumbnail_large":"thumbnail_large","name":"name","id":"id","title":"title","type":"type","url":"url"},"attachment":{"date":"date","thumbnail_small":"thumbnail_small","thumbnail_medium":"thumbnail_medium","size":0,"thumbnail_large":"thumbnail_large","mimetype":"mimetype","id":"id","title":"title","url":"url"},"text":"text","type":"type","frame":{"id":"id","url":"url"}}],"id":"id"}
                    ],
                creation_time = '',
                creator = '',
                description = '',
                due_time = '',
                id = '',
                name = '',
                organization_id = '',
                priority = 'LOW',
                status = 'OPEN',
                watchers = [
                    ''
                    ]
            )
        else:
            return SupportTicket(
        )
        """

    def testSupportTicket(self):
        """Test SupportTicket"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()