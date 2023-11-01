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

from openapi_client.models.workload_meta_info import WorkloadMetaInfo  # noqa: E501

class TestWorkloadMetaInfo(unittest.TestCase):
    """WorkloadMetaInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkloadMetaInfo:
        """Test WorkloadMetaInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkloadMetaInfo`
        """
        model = WorkloadMetaInfo()  # noqa: E501
        if include_optional:
            return WorkloadMetaInfo(
                base_agreement_id = '',
                buyer_ids = [
                    ''
                    ],
                contacts = [
                    openapi_client.models.contact.Contact(
                        company = '', 
                        email = '', 
                        name = '', )
                    ],
                custom_meta_info = {
                    'key' : ''
                    },
                error_messages = [
                    ''
                    ],
                hubspot_deal_id = '',
                internal_note = '',
                is_agreement_based_offer = True,
                is_renewal_offer = True,
                notifications = [
                    openapi_client.models.notification_event.NotificationEvent(
                        action = 'ACCEPT', 
                        cc_contact_ids = [
                            ''
                            ], 
                        contact_ids = [
                            ''
                            ], 
                        entity_id = '', 
                        entity_status = '', 
                        entity_type = 'ORGANIZATION', 
                        event_id = '', 
                        event_status = openapi_client.models.event_status.eventStatus(), 
                        last_update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        message = '', 
                        organization_id = '', 
                        partner = openapi_client.models.partner.partner(), 
                        timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        title = '', 
                        track_events = [
                            openapi_client.models.track_event.TrackEvent(
                                contact_id = '', 
                                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                            ], )
                    ],
                renewal_offer_type = '',
                salesforce_opportunity_id = ''
            )
        else:
            return WorkloadMetaInfo(
        )
        """

    def testWorkloadMetaInfo(self):
        """Test WorkloadMetaInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
