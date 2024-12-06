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
**amount** | **float** |  | [optional] 
**billable_dimension_details** | [**List[BillableDimensionPriceModelDetail]**](BillableDimensionPriceModelDetail.md) |  | [optional] 
**commits_revenue_details** | [**List[CommitRevenueDetail]**](CommitRevenueDetail.md) | Recurring flat fee for the invoice. There should be only one type fee for each invoice, commits, or usage. | [optional] 
**creation_date** | **datetime** | The creation date of the invoice when the status of the invoice may be draft or issued. It may be different from the issue date. | [optional] 
**currency** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**due_date** | **datetime** | DueDate &#x3D; IssueDate + NetTerm | [optional] 
**grace_period_in_days** | **int** | Grace Period in number of days | [optional] 
**issue_date** | **datetime** | IssueDate, issue invoice automatically when CreationDate + GracePeriod, or issue invoice manually IssueDate &gt;&#x3D; CreationDate &amp;&amp; IssueDate &lt;&#x3D; CreationDate + GracePeriod | [optional] 
**memo** | **str** |  | [optional] 
**net_terms_in_days** | **int** | Net Terms period in number of days | [optional] 
**payment_installments_detail** | [**BillingPaymentInstallmentDetail**](BillingPaymentInstallmentDetail.md) |  | [optional] 
**receipt_url** | **str** | Invoice receipt url, it only exists when there are transactions. | [optional] 
**spa_url** | **str** | SPA url with JWT. | [optional] 
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


