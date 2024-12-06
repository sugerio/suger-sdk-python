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

from suger_sdk_python.models.list_revenue_records_response import ListRevenueRecordsResponse

class TestListRevenueRecordsResponse(unittest.TestCase):
    """ListRevenueRecordsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListRevenueRecordsResponse:
        """Test ListRevenueRecordsResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListRevenueRecordsResponse`
        """
        model = ListRevenueRecordsResponse()
        if include_optional:
            return ListRevenueRecordsResponse(
                next_offset = 56,
                revenue_records = [
                    {"date":"2000-01-23T04:56:07.000+00:00","amount":0.8008281904610115,"productID":"productID","refundDisburseAmount":9.965781217890562,"entitlementID":"entitlementID","invoiceAmount":5.025004791520295,"buyerID":"buyerID","invoiceDate":"2000-01-23T04:56:07.000+00:00","collectableAmount":6.027456183070403,"disburseDate":"2000-01-23T04:56:07.000+00:00","refundInvoiceDate":"2000-01-23T04:56:07.000+00:00","refundDisburseDate":"2000-01-23T04:56:07.000+00:00","organizationID":"organizationID","paymentDueDate":"2000-01-23T04:56:07.000+00:00","refundInvoiceAmount":9.369310271410669,"partner":"partner","currency":"currency","disburseAmount":1.4658129805029452,"id":"id","taxAmount":6.683562403749608,"info":{"awsRevenueRecords":[{"brokerID":"brokerID","usagePeriodStartDate":{"valid":true,"time":"time"},"productID":"productID","insertDate":{"valid":true,"time":"time"},"toAccountID":"toAccountID","usagePeriodEndDate":{"valid":true,"time":"time"},"parentBillingEventID":"parentBillingEventID","disbursementBillingEventID":"disbursementBillingEventID","action":"action","offerID":"offerID","currency":"currency","invoiceID":"invoiceID","id":"id","balanceImpacting":5,"amount":5.962133916683182,"endUserAccountID":"endUserAccountID","dataFeedProductID":"dataFeedProductID","entitlementID":"entitlementID","buyerID":"buyerID","invoiceDate":{"valid":true,"time":"time"},"transactionReferenceID":"transactionReferenceID","organizationID":"organizationID","transactionType":"transactionType","paymentDueDate":{"valid":true,"time":"time"},"fromAccountID":"fromAccountID","agreementID":"agreementID","billingAddressID":"billingAddressID","bankTraceID":"bankTraceID"},{"brokerID":"brokerID","usagePeriodStartDate":{"valid":true,"time":"time"},"productID":"productID","insertDate":{"valid":true,"time":"time"},"toAccountID":"toAccountID","usagePeriodEndDate":{"valid":true,"time":"time"},"parentBillingEventID":"parentBillingEventID","disbursementBillingEventID":"disbursementBillingEventID","action":"action","offerID":"offerID","currency":"currency","invoiceID":"invoiceID","id":"id","balanceImpacting":5,"amount":5.962133916683182,"endUserAccountID":"endUserAccountID","dataFeedProductID":"dataFeedProductID","entitlementID":"entitlementID","buyerID":"buyerID","invoiceDate":{"valid":true,"time":"time"},"transactionReferenceID":"transactionReferenceID","organizationID":"organizationID","transactionType":"transactionType","paymentDueDate":{"valid":true,"time":"time"},"fromAccountID":"fromAccountID","agreementID":"agreementID","billingAddressID":"billingAddressID","bankTraceID":"bankTraceID"}],"disbursementNotificationSent":true,"azureRevenueRecords":[{"purchaseRecordID":"purchaseRecordID","revenueUsd":7.061401241503109,"productID":"productID","termEndDate":"termEndDate","azureBillingAccountID":"azureBillingAccountID","azureCustomerID":"azureCustomerID","billingModel":"billingModel","entitlementID":"entitlementID","payoutStatus":"payoutStatus","buyerID":"buyerID","organizationID":"organizationID","termStartDate":"termStartDate","azureAssetID":"azureAssetID","offerID":"offerID","earningUsd":2.3021358869347655,"azureOfferID":"azureOfferID","azurePlanID":"azurePlanID","estimatedPayoutMonth":{"valid":true,"time":"time"},"paymentSentDate":{"valid":true,"time":"time"}},{"purchaseRecordID":"purchaseRecordID","revenueUsd":7.061401241503109,"productID":"productID","termEndDate":"termEndDate","azureBillingAccountID":"azureBillingAccountID","azureCustomerID":"azureCustomerID","billingModel":"billingModel","entitlementID":"entitlementID","payoutStatus":"payoutStatus","buyerID":"buyerID","organizationID":"organizationID","termStartDate":"termStartDate","azureAssetID":"azureAssetID","offerID":"offerID","earningUsd":2.3021358869347655,"azureOfferID":"azureOfferID","azurePlanID":"azurePlanID","estimatedPayoutMonth":{"valid":true,"time":"time"},"paymentSentDate":{"valid":true,"time":"time"}}],"resource":"resource","idSource":"idSource","creditAmount":9.301444243932576,"gcpRevenueRecords":[{"productID":"productID","usage":1.1730742509559433,"withheld":4.965218492984954,"paymentType":"paymentType","accountID":"accountID","refundBalanceOutstanding":1.4894159098541704,"reportDate":"reportDate","trialUse":7.457744773683766,"paymentSchedule":"paymentSchedule","offerID":"offerID","currency":"currency","prepayCredits":1.2315135367772556,"abandoned":3.616076749251911,"sku":"sku","released":6.84685269835264,"usedBy":"usedBy","insightAccountID":"insightAccountID","dueVendor":4.145608029883936,"resource":"resource","googleEntity":"googleEntity","refundReason":"refundReason","entitlementID":"entitlementID","buyerID":"buyerID","organizationID":"organizationID","charges":2.027123023002322,"unit":"unit","refundBalanceDeductedThisMonth":1.0246457001441578,"ordinal":7},{"productID":"productID","usage":1.1730742509559433,"withheld":4.965218492984954,"paymentType":"paymentType","accountID":"accountID","refundBalanceOutstanding":1.4894159098541704,"reportDate":"reportDate","trialUse":7.457744773683766,"paymentSchedule":"paymentSchedule","offerID":"offerID","currency":"currency","prepayCredits":1.2315135367772556,"abandoned":3.616076749251911,"sku":"sku","released":6.84685269835264,"usedBy":"usedBy","insightAccountID":"insightAccountID","dueVendor":4.145608029883936,"resource":"resource","googleEntity":"googleEntity","refundReason":"refundReason","entitlementID":"entitlementID","buyerID":"buyerID","organizationID":"organizationID","charges":2.027123023002322,"unit":"unit","refundBalanceDeductedThisMonth":1.0246457001441578,"ordinal":7}]}}
                    ]
            )
        else:
            return ListRevenueRecordsResponse(
        )
        """

    def testListRevenueRecordsResponse(self):
        """Test ListRevenueRecordsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
