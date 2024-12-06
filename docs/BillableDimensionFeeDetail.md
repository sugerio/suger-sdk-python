# BillableDimensionFeeDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**descriptions** | **str** | Description of the pricing model that is used to show what the amount is for. like &#39;Bulk pricing: 0-100 units&#39;, &#39;Tiered pricing: 0-100 units&#39; | [optional] 
**fee_expressions** | **str** | FeeExpression is the expression used to calculate the fee that is used to show how the amount is calculated. like &#39;211 × $0.03&#39; | [optional] 

## Example

```python
from suger_sdk_python.models.billable_dimension_fee_detail import BillableDimensionFeeDetail

# TODO update the JSON string below
json = "{}"
# create an instance of BillableDimensionFeeDetail from a JSON string
billable_dimension_fee_detail_instance = BillableDimensionFeeDetail.from_json(json)
# print the JSON string representation of the object
print(BillableDimensionFeeDetail.to_json())

# convert the object into a dict
billable_dimension_fee_detail_dict = billable_dimension_fee_detail_instance.to_dict()
# create an instance of BillableDimensionFeeDetail from a dict
billable_dimension_fee_detail_from_dict = BillableDimensionFeeDetail.from_dict(billable_dimension_fee_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


