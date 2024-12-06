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

from suger_sdk_python.models.workload_entitlement_term import WorkloadEntitlementTerm

class TestWorkloadEntitlementTerm(unittest.TestCase):
    """WorkloadEntitlementTerm unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkloadEntitlementTerm:
        """Test WorkloadEntitlementTerm
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkloadEntitlementTerm`
        """
        model = WorkloadEntitlementTerm()
        if include_optional:
            return WorkloadEntitlementTerm(
                buyer_id = '',
                commit_amount = 1.337,
                credit_amount = 1.337,
                end_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                entitlement_id = '',
                entitlement_info = {"alibabaOrders":[{"PaidOn":1,"CouponPrice":2.027123023002322,"PeriodType":"PeriodType","OriginalPrice":1.2315135367772556,"PayStatus":"PayStatus","ProductName":"ProductName","RequestId":"RequestId","ProductCode":"ProductCode","SupplierCompanyName":"SupplierCompanyName","Quantity":6,"OrderId":7,"SupplierTelephones":{"Telephone":["Telephone","Telephone"]},"Components":{"key":""},"OrderStatus":"OrderStatus","OrderType":"OrderType","TotalPrice":7.457744773683766,"ProductSkuCode":"ProductSkuCode","CreatedOn":4,"PaymentPrice":1.4894159098541704,"InstanceIds":{"InstanceId":["InstanceId","InstanceId"]},"AccountQuantity":9,"AliUid":3},{"PaidOn":1,"CouponPrice":2.027123023002322,"PeriodType":"PeriodType","OriginalPrice":1.2315135367772556,"PayStatus":"PayStatus","ProductName":"ProductName","RequestId":"RequestId","ProductCode":"ProductCode","SupplierCompanyName":"SupplierCompanyName","Quantity":6,"OrderId":7,"SupplierTelephones":{"Telephone":["Telephone","Telephone"]},"Components":{"key":""},"OrderStatus":"OrderStatus","OrderType":"OrderType","TotalPrice":7.457744773683766,"ProductSkuCode":"ProductSkuCode","CreatedOn":4,"PaymentPrice":1.4894159098541704,"InstanceIds":{"InstanceId":["InstanceId","InstanceId"]},"AccountQuantity":9,"AliUid":3}],"invoicedAmount":9.018348186070783,"addons":[{"amount":0.8008281904610115,"name":"name","description":"description","chargeOn":"2000-01-23T04:56:07.000+00:00","id":"id"},{"amount":0.8008281904610115,"name":"name","description":"description","chargeOn":"2000-01-23T04:56:07.000+00:00","id":"id"}],"trialConfig":"{}","azureSubscriptions":[{"fulfillmentId":"fulfillmentId","quantity":1,"allowedCustomerOperations":["Read","Read"],"created":"2000-01-23T04:56:07.000+00:00","purchaser":{"firstName":"firstName","lastName":"lastName","licenseType":"licenseType","puid":"puid","customerId":"customerId","tenantId":"tenantId","billingAccountId":"billingAccountId","emailId":"emailId","objectId":"objectId"},"isFreeTrial":true,"sessionId":"sessionId","saasSubscriptionStatus":"NotStarted","publisherId":"publisherId","beneficiary":{"firstName":"firstName","lastName":"lastName","licenseType":"licenseType","puid":"puid","customerId":"customerId","tenantId":"tenantId","billingAccountId":"billingAccountId","emailId":"emailId","objectId":"objectId"},"isTest":true,"name":"name","autoRenew":true,"offerId":"offerId","planId":"planId","storeFront":"storeFront","term":{"endDate":"2000-01-23T04:56:07.000+00:00","chargeDuration":"chargeDuration","startDate":"2000-01-23T04:56:07.000+00:00","termUnit":"termUnit"},"id":"id","lastModified":"lastModified","sandboxType":"None","sessionMode":"None"},{"fulfillmentId":"fulfillmentId","quantity":1,"allowedCustomerOperations":["Read","Read"],"created":"2000-01-23T04:56:07.000+00:00","purchaser":{"firstName":"firstName","lastName":"lastName","licenseType":"licenseType","puid":"puid","customerId":"customerId","tenantId":"tenantId","billingAccountId":"billingAccountId","emailId":"emailId","objectId":"objectId"},"isFreeTrial":true,"sessionId":"sessionId","saasSubscriptionStatus":"NotStarted","publisherId":"publisherId","beneficiary":{"firstName":"firstName","lastName":"lastName","licenseType":"licenseType","puid":"puid","customerId":"customerId","tenantId":"tenantId","billingAccountId":"billingAccountId","emailId":"emailId","objectId":"objectId"},"isTest":true,"name":"name","autoRenew":true,"offerId":"offerId","planId":"planId","storeFront":"storeFront","term":{"endDate":"2000-01-23T04:56:07.000+00:00","chargeDuration":"chargeDuration","startDate":"2000-01-23T04:56:07.000+00:00","termUnit":"termUnit"},"id":"id","lastModified":"lastModified","sandboxType":"None","sessionMode":"None"}],"awsEntitlements":[{"productCode":"productCode","customerIdentifier":"customerIdentifier","dimension":"dimension","value":"{}","expirationDate":"expirationDate"},{"productCode":"productCode","customerIdentifier":"customerIdentifier","dimension":"dimension","value":"{}","expirationDate":"expirationDate"}],"gcpEntitlements":[{"newPendingOffer":"newPendingOffer","offerEffectiveTime":"2000-01-23T04:56:07.000+00:00","newPlan":"newPlan","offer":"offer","inputProperties":[9,9],"provider":"provider","offerEndTime":"2000-01-23T04:56:07.000+00:00","offerDuration":"offerDuration","consumers":[{"project":"project"},{"project":"project"}],"newOfferEndTime":"newOfferEndTime","subscriptionEndTime":"2000-01-23T04:56:07.000+00:00","id":"id","state":"{}","usageReportingId":"usageReportingId","plan":"plan","messageToUser":"messageToUser","product":"product","updateTime":"2000-01-23T04:56:07.000+00:00","newOfferDuration":"newOfferDuration","quoteExternalName":"quoteExternalName","createTime":"2000-01-23T04:56:07.000+00:00","newPendingPlan":"newPendingPlan","name":"name","newPendingOfferDuration":"newPendingOfferDuration","account":"account","productExternalName":"productExternalName","newOfferStartTime":"newOfferStartTime"},{"newPendingOffer":"newPendingOffer","offerEffectiveTime":"2000-01-23T04:56:07.000+00:00","newPlan":"newPlan","offer":"offer","inputProperties":[9,9],"provider":"provider","offerEndTime":"2000-01-23T04:56:07.000+00:00","offerDuration":"offerDuration","consumers":[{"project":"project"},{"project":"project"}],"newOfferEndTime":"newOfferEndTime","subscriptionEndTime":"2000-01-23T04:56:07.000+00:00","id":"id","state":"{}","usageReportingId":"usageReportingId","plan":"plan","messageToUser":"messageToUser","product":"product","updateTime":"2000-01-23T04:56:07.000+00:00","newOfferDuration":"newOfferDuration","quoteExternalName":"quoteExternalName","createTime":"2000-01-23T04:56:07.000+00:00","newPendingPlan":"newPendingPlan","name":"name","newPendingOfferDuration":"newPendingOfferDuration","account":"account","productExternalName":"productExternalName","newOfferStartTime":"newOfferStartTime"}],"paymentInstallments":[{"discountPercentage":8.762042012749001,"amount":9.369310271410669,"originalAmount":9.018348186070783,"chargeOn":"2000-01-23T04:56:07.000+00:00","chargeOnStr":"chargeOnStr","credit":6.683562403749608},{"discountPercentage":8.762042012749001,"amount":9.369310271410669,"originalAmount":9.018348186070783,"chargeOn":"2000-01-23T04:56:07.000+00:00","chargeOnStr":"chargeOnStr","credit":6.683562403749608}],"billableDimensions":[{"priceModelTiered":"{}","priceModelTieredPercentage":"{}","priceModelMatrix":"{}","minimumCommit":1.4658129805029452,"length":6,"priceModelBulk":"{}","description":"description","discount":"{}","minimumCommitScope":"{}","minimumCommitProrata":true,"billableMetricId":"billableMetricId","priceModelPercentage":"{}","name":"name","priceModelBasic":"{}","category":"{}","priceModelVolume":"{}","timeUnit":"{}"},{"priceModelTiered":"{}","priceModelTieredPercentage":"{}","priceModelMatrix":"{}","minimumCommit":1.4658129805029452,"length":6,"priceModelBulk":"{}","description":"description","discount":"{}","minimumCommitScope":"{}","minimumCommitProrata":true,"billableMetricId":"billableMetricId","priceModelPercentage":"{}","name":"name","priceModelBasic":"{}","category":"{}","priceModelVolume":"{}","timeUnit":"{}"}],"eulaUrl":"eulaUrl","refundCancellationPolicy":"refundCancellationPolicy","paymentSchedule":"{}","autoRenew":true,"currency":"currency","alibabaEntitlements":[{"Status":"Status","ProductName":"ProductName","EndOn":5,"InstanceId":2,"ProductCode":"ProductCode","Modules":{"Module":[{"Id":"Id","Properties":{"Property":[{"PropertyValues":{"PropertyValue":[{"Type":"Type","Min":"Min","Max":"Max","DisplayName":"DisplayName","Value":"Value","Step":"Step","Remark":"Remark"},{"Type":"Type","Min":"Min","Max":"Max","DisplayName":"DisplayName","Value":"Value","Step":"Step","Remark":"Remark"}]},"DisplayUnit":"DisplayUnit","Key":"Key","Name":"Name","ShowType":"ShowType"},{"PropertyValues":{"PropertyValue":[{"Type":"Type","Min":"Min","Max":"Max","DisplayName":"DisplayName","Value":"Value","Step":"Step","Remark":"Remark"},{"Type":"Type","Min":"Min","Max":"Max","DisplayName":"DisplayName","Value":"Value","Step":"Step","Remark":"Remark"}]},"DisplayUnit":"DisplayUnit","Key":"Key","Name":"Name","ShowType":"ShowType"}]},"Code":"Code","Name":"Name"},{"Id":"Id","Properties":{"Property":[{"PropertyValues":{"PropertyValue":[{"Type":"Type","Min":"Min","Max":"Max","DisplayName":"DisplayName","Value":"Value","Step":"Step","Remark":"Remark"},{"Type":"Type","Min":"Min","Max":"Max","DisplayName":"DisplayName","Value":"Value","Step":"Step","Remark":"Remark"}]},"DisplayUnit":"DisplayUnit","Key":"Key","Name":"Name","ShowType":"ShowType"},{"PropertyValues":{"PropertyValue":[{"Type":"Type","Min":"Min","Max":"Max","DisplayName":"DisplayName","Value":"Value","Step":"Step","Remark":"Remark"},{"Type":"Type","Min":"Min","Max":"Max","DisplayName":"DisplayName","Value":"Value","Step":"Step","Remark":"Remark"}]},"DisplayUnit":"DisplayUnit","Key":"Key","Name":"Name","ShowType":"ShowType"}]},"Code":"Code","Name":"Name"}]},"RelationalData":{"ServiceStatus":"ServiceStatus"},"AppJson":"AppJson","ProductType":"ProductType","OrderId":7,"Constraints":"Constraints","AutoRenewal":"AutoRenewal","ExtendJson":"ExtendJson","ComponentJson":"ComponentJson","IsTrial":true,"SupplierName":"SupplierName","ProductSkuCode":"ProductSkuCode","CreatedOn":5,"HostJson":"HostJson","BeganOn":1},{"Status":"Status","ProductName":"ProductName","EndOn":5,"InstanceId":2,"ProductCode":"ProductCode","Modules":{"Module":[{"Id":"Id","Properties":{"Property":[{"PropertyValues":{"PropertyValue":[{"Type":"Type","Min":"Min","Max":"Max","DisplayName":"DisplayName","Value":"Value","Step":"Step","Remark":"Remark"},{"Type":"Type","Min":"Min","Max":"Max","DisplayName":"DisplayName","Value":"Value","Step":"Step","Remark":"Remark"}]},"DisplayUnit":"DisplayUnit","Key":"Key","Name":"Name","ShowType":"ShowType"},{"PropertyValues":{"PropertyValue":[{"Type":"Type","Min":"Min","Max":"Max","DisplayName":"DisplayName","Value":"Value","Step":"Step","Remark":"Remark"},{"Type":"Type","Min":"Min","Max":"Max","DisplayName":"DisplayName","Value":"Value","Step":"Step","Remark":"Remark"}]},"DisplayUnit":"DisplayUnit","Key":"Key","Name":"Name","ShowType":"ShowType"}]},"Code":"Code","Name":"Name"},{"Id":"Id","Properties":{"Property":[{"PropertyValues":{"PropertyValue":[{"Type":"Type","Min":"Min","Max":"Max","DisplayName":"DisplayName","Value":"Value","Step":"Step","Remark":"Remark"},{"Type":"Type","Min":"Min","Max":"Max","DisplayName":"DisplayName","Value":"Value","Step":"Step","Remark":"Remark"}]},"DisplayUnit":"DisplayUnit","Key":"Key","Name":"Name","ShowType":"ShowType"},{"PropertyValues":{"PropertyValue":[{"Type":"Type","Min":"Min","Max":"Max","DisplayName":"DisplayName","Value":"Value","Step":"Step","Remark":"Remark"},{"Type":"Type","Min":"Min","Max":"Max","DisplayName":"DisplayName","Value":"Value","Step":"Step","Remark":"Remark"}]},"DisplayUnit":"DisplayUnit","Key":"Key","Name":"Name","ShowType":"ShowType"}]},"Code":"Code","Name":"Name"}]},"RelationalData":{"ServiceStatus":"ServiceStatus"},"AppJson":"AppJson","ProductType":"ProductType","OrderId":7,"Constraints":"Constraints","AutoRenewal":"AutoRenewal","ExtendJson":"ExtendJson","ComponentJson":"ComponentJson","IsTrial":true,"SupplierName":"SupplierName","ProductSkuCode":"ProductSkuCode","CreatedOn":5,"HostJson":"HostJson","BeganOn":1}],"disbursedAmount":9.965781217890562,"netTermsInDays":6,"dimensionsOversized":true,"eulaType":"","gracePeriodInDays":6,"grossAmount":8.762042012749001,"gcpPlans":[{"priceInfo":{"usageFees":[{"priceTiers":[{"startingUsageAmount":"startingUsageAmount","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"},"fromAmount":7.386281948385884},{"startingUsageAmount":"startingUsageAmount","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"},"fromAmount":7.386281948385884}],"metricId":"metricId","displayQuantity":7},{"priceTiers":[{"startingUsageAmount":"startingUsageAmount","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"},"fromAmount":7.386281948385884},{"startingUsageAmount":"startingUsageAmount","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"},"fromAmount":7.386281948385884}],"metricId":"metricId","displayQuantity":7}],"subscriptionPlans":[{"period":"period","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"}},{"period":"period","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"}}],"description":"description","priceModel":"FREE"},"purchaseMode":"PURCHASE_MODE_PRIVATE","name":"name","title":"title","featureValues":[{"featureValue":"featureValue","featureTitle":"featureTitle","featureName":"featureName","featureDescription":"featureDescription"},{"featureValue":"featureValue","featureTitle":"featureTitle","featureName":"featureName","featureDescription":"featureDescription"}]},{"priceInfo":{"usageFees":[{"priceTiers":[{"startingUsageAmount":"startingUsageAmount","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"},"fromAmount":7.386281948385884},{"startingUsageAmount":"startingUsageAmount","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"},"fromAmount":7.386281948385884}],"metricId":"metricId","displayQuantity":7},{"priceTiers":[{"startingUsageAmount":"startingUsageAmount","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"},"fromAmount":7.386281948385884},{"startingUsageAmount":"startingUsageAmount","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"},"fromAmount":7.386281948385884}],"metricId":"metricId","displayQuantity":7}],"subscriptionPlans":[{"period":"period","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"}},{"period":"period","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"}}],"description":"description","priceModel":"FREE"},"purchaseMode":"PURCHASE_MODE_PRIVATE","name":"name","title":"title","featureValues":[{"featureValue":"featureValue","featureTitle":"featureTitle","featureName":"featureName","featureDescription":"featureDescription"},{"featureValue":"featureValue","featureTitle":"featureTitle","featureName":"featureName","featureDescription":"featureDescription"}]}],"collectableAmount":4.965218492984954,"alertDaysBeforeEnd":6,"sellerNotes":"sellerNotes","awsAgreement":"{}","billingCycle":"{}","commits":[{"types":["types","types"],"quantity":3,"length":2,"description":"description","type":"{}","maximumUsers":706140,"rate":2.027123023002322,"isUserCreated":true,"minimumUsers":930144,"name":"name","term":"term","category":"category","termEndTime":"termEndTime","key":"key","timeUnit":"{}"},{"types":["types","types"],"quantity":3,"length":2,"description":"description","type":"{}","maximumUsers":706140,"rate":2.027123023002322,"isUserCreated":true,"minimumUsers":930144,"name":"name","term":"term","category":"category","termEndTime":"termEndTime","key":"key","timeUnit":"{}"}],"awsChannelPartner":"{}","commitAmount":5.025004791520295,"dimensions":[{"priceTiers":[{"startingUsageAmount":"startingUsageAmount","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"},"fromAmount":7.386281948385884},{"startingUsageAmount":"startingUsageAmount","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"},"fromAmount":7.386281948385884}],"types":["types","types"],"description":"description","planName":"planName","usageCount":"{}","rate":1.0246457001441578,"includedBaseQuantities":[{"quantity":4.145608029883936,"isInfinite":true,"recurringUnit":"Monthly"},{"quantity":4.145608029883936,"isInfinite":true,"recurringUnit":"Monthly"}],"valueType":"{}","name":"name","planId":"planId","category":"category","key":"key","skuId":"skuId"},{"priceTiers":[{"startingUsageAmount":"startingUsageAmount","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"},"fromAmount":7.386281948385884},{"startingUsageAmount":"startingUsageAmount","price":{"nanos":1,"units":"units","currencyCode":"currencyCode"},"fromAmount":7.386281948385884}],"types":["types","types"],"description":"description","planName":"planName","usageCount":"{}","rate":1.0246457001441578,"includedBaseQuantities":[{"quantity":4.145608029883936,"isInfinite":true,"recurringUnit":"Monthly"},{"quantity":4.145608029883936,"isInfinite":true,"recurringUnit":"Monthly"}],"valueType":"{}","name":"name","planId":"planId","category":"category","key":"key","skuId":"skuId"}],"spaUrl":"spaUrl"},
                external_entitlement_id = '',
                id = '',
                info = {"dimensionQuantityDecimalParts":{"key":1.4658129805029452},"parentEntitlementTermId":"parentEntitlementTermId","type":"","subEntitlementTermIds":["subEntitlementTermIds","subEntitlementTermIds"],"isCommitDivided":true},
                offer_id = '',
                organization_id = '',
                partner = '',
                product_id = '',
                reported_amount = 1.337,
                service = 'DEFAULT',
                start_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                used_commit_amount = 1.337,
                used_credit_amount = 1.337
            )
        else:
            return WorkloadEntitlementTerm(
        )
        """

    def testWorkloadEntitlementTerm(self):
        """Test WorkloadEntitlementTerm"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
