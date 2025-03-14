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

from suger_sdk_python.models.identity_buyer import IdentityBuyer

class TestIdentityBuyer(unittest.TestCase):
    """IdentityBuyer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdentityBuyer:
        """Test IdentityBuyer
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdentityBuyer`
        """
        model = IdentityBuyer()
        if include_optional:
            return IdentityBuyer(
                contact_ids = [
                    ''
                    ],
                creation_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                description = '',
                external_id = '',
                id = '',
                info = {"stripeBuyer":"{}","invoicedAmount":5.962133916683182,"companyInfo":{"country":"country","emailDomain":"emailDomain","city":"city","postalCode":"postalCode","name":"name","addressLine1":"addressLine1","addressLine2":"addressLine2","state":"state","validFrom":"validFrom"},"gcpBuyer":"{}","lastModifiedBy":"lastModifiedBy","grossAmount":1.4658129805029452,"collectableAmount":0.8008281904610115,"paymentConfig":"{}","emailAddress":"emailAddress","orbCustomerId":"orbCustomerId","adyenBuyer":"{}","azureBuyer":"{}","customerId":"customerId","lagoCustomerId":"lagoCustomerId","awsBuyer":"{}","fields":{"key":""},"metronomeCustomerId":"metronomeCustomerId","stripeCustomerId":"stripeCustomerId","disbursedAmount":6.027456183070403,"spaUrl":"spaUrl"},
                last_update_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                name = '',
                organization_id = '',
                partner = ''
            )
        else:
            return IdentityBuyer(
        )
        """

    def testIdentityBuyer(self):
        """Test IdentityBuyer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
