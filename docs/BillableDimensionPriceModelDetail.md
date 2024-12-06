# BillableDimensionPriceModelDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount is the amount that is calculated based on the FeeExpression | [optional] 
**billable_metric_key** | [**MeteringUsageRecordGroupByKey**](MeteringUsageRecordGroupByKey.md) | BillableMetricKey is the key of the billable metric | [optional] 
**category** | [**PriceModelCategory**](PriceModelCategory.md) | Category of this billable dimension. | [optional] 
**details** | [**List[BillableDimensionFeeDetail]**](BillableDimensionFeeDetail.md) | Details is the details of the pricing model that is used to show what the amount is for. | [optional] 
**discount** | [**BillingDiscount**](BillingDiscount.md) | The discount of this billable dimension if applicable. | [optional] 
**discount_expression** | **str** | DiscountExpression is the expression used to calculate the discount that is used to show how the discount is calculated. | [optional] 
**is_trial** | **bool** | Flag to indicate if this period is a trial period. | [optional] 
**minimum_commit** | **float** | MinimumCommit is the minimum commit amount that is used to show the minimum commit amount. Will be ignored if the value is 0 or less. | [optional] 
**minimum_commit_scope** | [**BillingMinimumCommitScope**](BillingMinimumCommitScope.md) | The minimum commit scope. The default value is \&quot;DIMENSION\&quot; if not set. | [optional] 
**name** | **str** | Name of this billable dimension. | [optional] 
**quantity** | **float** | Final quantity of the billable dimension in the invoice period, which calculates the fee in price model. It may be the sum value of count/sum/unique_count or latest/max value according to different aggregation type. | [optional] 

## Example

```python
from suger_sdk_python.models.billable_dimension_price_model_detail import BillableDimensionPriceModelDetail

# TODO update the JSON string below
json = "{}"
# create an instance of BillableDimensionPriceModelDetail from a JSON string
billable_dimension_price_model_detail_instance = BillableDimensionPriceModelDetail.from_json(json)
# print the JSON string representation of the object
print(BillableDimensionPriceModelDetail.to_json())

# convert the object into a dict
billable_dimension_price_model_detail_dict = billable_dimension_price_model_detail_instance.to_dict()
# create an instance of BillableDimensionPriceModelDetail from a dict
billable_dimension_price_model_detail_from_dict = BillableDimensionPriceModelDetail.from_dict(billable_dimension_price_model_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


