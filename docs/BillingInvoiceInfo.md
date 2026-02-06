# BillingInvoiceInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_fixed_fees** | [**List[InvoiceAddFixedFee]**](InvoiceAddFixedFee.md) | Adjust charge fields The fixed fees to be added to the invoice. | [optional] 
**addon_detail** | [**BillingAddonRecord**](BillingAddonRecord.md) |  | [optional] 
**adjust_discount_by_dimensions** | [**List[InvoiceAdjustDiscountByDimension]**](InvoiceAdjustDiscountByDimension.md) | add or adjust discount for a specific dimension | [optional] 
**adjust_minimum_spend_by_dimensions** | [**List[InvoiceAdjustMinimumSpendByDimension]**](InvoiceAdjustMinimumSpendByDimension.md) | add or adjust minimum spend for a specific dimension | [optional] 
**adjust_overall_discount** | [**InvoiceAdjustOverallDiscount**](InvoiceAdjustOverallDiscount.md) | add or adjust overall discount calculate each dimension&#39;s discount first, then apply the overall discount | [optional] 
**adjust_overall_minimum_spend** | [**InvoiceAdjustOverallMinimumSpend**](InvoiceAdjustOverallMinimumSpend.md) | add or adjust overall minimum spend calculate each dimension&#39;s minimum spend first, then apply the overall minimum spend | [optional] 
**aws_invoice** | [**AwsInvoice**](AwsInvoice.md) |  | [optional] 
**billable_dimension_details** | [**List[BillableDimensionPriceModelDetail]**](BillableDimensionPriceModelDetail.md) |  | [optional] 
**commits_revenue_details** | [**List[CommitRevenueDetail]**](CommitRevenueDetail.md) | Recurring flat fee for the invoice. There should be only one type fee for each invoice, commits, or usage. | [optional] 
**creation_date** | **datetime** | The creation date of the invoice when the status of the invoice may be draft or issued. It may be different from the issue date. | [optional] 
**currency** | **str** | Deprecated: Use BillingInvoice.Currency instead. | [optional] 
**deducted_commit_amount** | **float** | The amount of the committed amount that has been deducted from the usage. It works only when IsMeteringOverageCommit is true. | [optional] 
**deducted_commit_invoice_id** | **str** | The ID of the commit invoice that has been deducted from the usage. It works only when IsMeteringOverageCommit is true. | [optional] 
**description** | **str** |  | [optional] 
**due_amount** | **float** | Due amount &#x3D; SubtotalAmount + TaxAmount - AdjustOverallDiscount Deprecated: Use BillingInvoice.DueAmount instead. | [optional] 
**due_date** | **datetime** | DueDate &#x3D; IssueDate + NetTerm Deprecated: Use BillingInvoice.DueDate instead. | [optional] 
**grace_period_in_days** | **int** | Grace Period in number of days | [optional] 
**is_metering_overage_commit** | **bool** | Custom fields for Suger managed Stripe invoice. Whether the usage metering is charged for the amount that exceeds the committed amount from the entitlement. | [optional] 
**issue_date** | **datetime** | IssueDate, issue invoice automatically when CreationDate + GracePeriod, or issue invoice manually IssueDate &gt;&#x3D; CreationDate &amp;&amp; IssueDate &lt;&#x3D; CreationDate + GracePeriod Deprecated: Use BillingInvoice.IssueDate instead. | [optional] 
**memo** | **str** |  | [optional] 
**net_terms_in_days** | **int** | Net Terms period in number of days | [optional] 
**payment_installments_detail** | [**BillingPaymentInstallmentDetail**](BillingPaymentInstallmentDetail.md) |  | [optional] 
**pdf_url** | **str** | The PDF URL of the invoice, provided as AWS S3 presigned URL. Output only. | [optional] 
**period_total_days** | **int** | PeriodTotalDays is the total number of days among the whole periods. e.g. 61 days for a 2-month invoice. | [optional] 
**receipt_url** | **str** | Invoice receipt url, it only exists when there are transactions. | [optional] 
**related_entitlement_ids** | **List[str]** | The IDs of the entitlements related to the invoice. Aws invoice may be related to multiple entitlements. | [optional] 
**spa_url** | **str** | SPA url with JWT. | [optional] 
**subtotal_amount** | **float** | Fields designed for stripe invoice. Subtotal amount calculated from the user usage. Deprecated: Use BillingInvoice.TotalAmount instead. | [optional] 
**tax_amount** | **float** |  | [optional] 
**trial_period_in_days** | **int** | Trial period in number of days | [optional] 
**usage_daily_revenues** | [**List[BillableDimensionUsageDailyRevenue]**](BillableDimensionUsageDailyRevenue.md) | Billable dimension fees for the invoice. | [optional] 

## Example

```python
from suger_sdk_python.models.billing_invoice_info import BillingInvoiceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BillingInvoiceInfo from a JSON string
billing_invoice_info_instance = BillingInvoiceInfo.from_json(json)
# print the JSON string representation of the object
print(BillingInvoiceInfo.to_json())

# convert the object into a dict
billing_invoice_info_dict = billing_invoice_info_instance.to_dict()
# create an instance of BillingInvoiceInfo from a dict
billing_invoice_info_from_dict = BillingInvoiceInfo.from_dict(billing_invoice_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


