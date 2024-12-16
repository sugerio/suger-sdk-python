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

from suger_sdk_python.models.support_ticket_comment import SupportTicketComment

class TestSupportTicketComment(unittest.TestCase):
    """SupportTicketComment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SupportTicketComment:
        """Test SupportTicketComment
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SupportTicketComment`
        """
        model = SupportTicketComment()
        if include_optional:
            return SupportTicketComment(
                comment = [
                    {"image":{"thumbnail_small":"thumbnail_small","extension":"extension","thumbnail_medium":"thumbnail_medium","thumbnail_large":"thumbnail_large","name":"name","id":"id","title":"title","type":"type","url":"url"},"attachment":{"date":"date","thumbnail_small":"thumbnail_small","thumbnail_medium":"thumbnail_medium","size":0,"thumbnail_large":"thumbnail_large","mimetype":"mimetype","id":"id","title":"title","url":"url"},"text":"text","type":"type","frame":{"id":"id","url":"url"}}
                    ],
                comment_text = '',
                creator = suger_sdk_python.models.support_ticket_user.SupportTicketUser(
                    email = '', 
                    id = '', 
                    is_suger_employee = True, 
                    profile_picture = '', 
                    username = '', ),
                var_date = '',
                id = ''
            )
        else:
            return SupportTicketComment(
        )
        """

    def testSupportTicketComment(self):
        """Test SupportTicketComment"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()