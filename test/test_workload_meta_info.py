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

from suger_sdk_python.models.workload_meta_info import WorkloadMetaInfo

class TestWorkloadMetaInfo(unittest.TestCase):
    """WorkloadMetaInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkloadMetaInfo:
        """Test WorkloadMetaInfo
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkloadMetaInfo`
        """
        model = WorkloadMetaInfo()
        if include_optional:
            return WorkloadMetaInfo(
                ace_apn_crm_unique_identifier = '',
                aws_saas_product_dimensions = [
                    {"Types":["Types","Types"],"Description":"Description","Length":6,"Rate":1.284659006116532,"TimeUnit":"DAY","Unit":"Unit","Key":"Key","Name":"Name"}
                    ],
                base_agreement_id = '',
                buyer_ids = [
                    ''
                    ],
                contacts = [
                    {"name":"name","company":"company","email":"email"}
                    ],
                cppo_in_offer_id = '',
                cppo_offer_id = '',
                cppo_out_offer_id = '',
                custom_meta_info = {
                    'key' : ''
                    },
                enable_test_usage_metering = True,
                entitlement_cancellation_schedule = {"note":"note","cancelDate":"cancelDate","creationDate":"creationDate","type":"{}"},
                error_messages = [
                    ''
                    ],
                hubspot_deal_id = '',
                internal_note = '',
                is_agreement_based_offer = True,
                is_gross_revenue_full_sync = True,
                is_renewal_offer = True,
                is_replacement_offer = True,
                last_modified_by = suger_sdk_python.models.last_modified_by.LastModifiedBy(
                    email = '', 
                    entity_id = '', 
                    entity_type = suger_sdk_python.models.entity_type.entityType(), 
                    name = '', ),
                notifications = [
                    {"eventID":"eventID","customFields":{"key":""},"entityType":"","contactEmails":["contactEmails","contactEmails"],"entityID":"entityID","message":"message","priority":"{}","title":"title","contactIds":["contactIds","contactIds"],"organizationID":"organizationID","ccContactIds":["ccContactIds","ccContactIds"],"channels":["EMAIL","EMAIL"],"isActionItem":true,"partner":"{}","createdBy":"{}","entityStatus":"entityStatus","entityName":"entityName","eventStatus":"{}","action":"","requireAudit":true,"trackEvents":[{"contactId":"contactId","action":"OPEN_EMAIL","timestamp":"2000-01-23T04:56:07.000+00:00"},{"contactId":"contactId","action":"OPEN_EMAIL","timestamp":"2000-01-23T04:56:07.000+00:00"}],"info":"{}","lastUpdateTime":"2000-01-23T04:56:07.000+00:00","timestamp":"2000-01-23T04:56:07.000+00:00"}
                    ],
                offer_accept_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                renewal_offer_type = '',
                replaced_offer_end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                replaced_offer_resource_name = '',
                salesforce_entitlement_url = '',
                salesforce_opportunity_id = '',
                test_usage_metering_end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                update_message = ''
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
