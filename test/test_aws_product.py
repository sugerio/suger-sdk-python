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

from suger_sdk_python.models.aws_product import AwsProduct

class TestAwsProduct(unittest.TestCase):
    """AwsProduct unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AwsProduct:
        """Test AwsProduct
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AwsProduct`
        """
        model = AwsProduct()
        if include_optional:
            return AwsProduct(
                description = {"UsW9Submitted":true,"Highlights":["Highlights","Highlights"],"Categories":["Categories","Categories"],"ProductCode":"ProductCode","SearchKeywords":["SearchKeywords","SearchKeywords"],"ProductTitle":"ProductTitle","EuW8Submitted":true,"ShortDescription":"ShortDescription","LongDescription":"LongDescription","Manufacturer":"Manufacturer","Visibility":"Limited","AssociatedProducts":"{}","Sku":"Sku","Registered":true},
                dimensions = [
                    {"Types":["Types","Types"],"Description":"Description","Length":3,"Rate":6.965117697638846,"TimeUnit":"DAY","Unit":"Unit","Key":"Key","Name":"Name"}
                    ],
                promotional_resources = {"AdditionalResources":[{"Type":"Type","Text":"Text","Url":"Url"},{"Type":"Type","Text":"Text","Url":"Url"}],"LogoUrl":"LogoUrl","VideoUrls":["VideoUrls","VideoUrls"]},
                repositories = [
                    {"Type":"Type","Url":"Url"}
                    ],
                signature_verification_keys = [
                    {"Status":"Status","PublicKey":"PublicKey","PublicKeyVersion":2}
                    ],
                support_information = {"Description":"Description"},
                versions = [
                    {"CreationDate":"2000-01-23T04:56:07.000+00:00","Id":"Id","DeliveryOptions":[{"Recommendations":"{}","Type":"Type","AmiAlias":"AmiAlias","SourceId":"SourceId","Title":"Title","Visibility":"Visibility","FulfillmentUrl":"FulfillmentUrl","Id":"Id","ShortDescription":"ShortDescription"},{"Recommendations":"{}","Type":"Type","AmiAlias":"AmiAlias","SourceId":"SourceId","Title":"Title","Visibility":"Visibility","FulfillmentUrl":"FulfillmentUrl","Id":"Id","ShortDescription":"ShortDescription"}],"ReleaseNotes":"ReleaseNotes","VersionTitle":"VersionTitle"}
                    ],
                data_feed_product_id = '',
                product_id = ''
            )
        else:
            return AwsProduct(
        )
        """

    def testAwsProduct(self):
        """Test AwsProduct"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()