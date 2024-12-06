# BillableDimension


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billable_metric_id** | **str** | The ID for the billable metric. | [optional] 
**category** | [**PriceModelCategory**](PriceModelCategory.md) | The category of the pricing model. This is used to determine which pricing model to use. | [optional] 
**description** | **str** | Description of the dimension. This is used in the UI to display the dimension. | [optional] 
**discount** | [**BillingDiscount**](BillingDiscount.md) | Discount for the dimension. | [optional] 
**length** | **int** | The term length for the commit amount. Applicable to Direct only. | [optional] 
**minimum_commit** | **float** | The minimum commit amount. Applicable to Direct only. Ignored if the value is 0 or less. | [optional] 
**minimum_commit_prorata** | **bool** | If the minimum commit is appled with pro-rata. Applicable to Direct only. If true, the minimum commit amount will be prorated based on the usage period (starting time and ending time). | [optional] 
**minimum_commit_scope** | [**BillingMinimumCommitScope**](BillingMinimumCommitScope.md) | The minimum commit scope. The default value is \&quot;DIMENSION\&quot; if not set. | [optional] 
**name** | **str** | Display name of the dimension. This is used in the UI to display the dimension. | [optional] 
**price_model_basic** | [**PriceModelBasic**](PriceModelBasic.md) | The configuration for the Basic pricing model. Applicable to Direct only. | [optional] 
**price_model_bulk** | [**PriceModelBulk**](PriceModelBulk.md) | The configuration for the Package pricing model. Applicable to Direct only. | [optional] 
**price_model_matrix** | [**PriceModelMatrix**](PriceModelMatrix.md) | The configuration for the Matrix pricing model. Applicable to Direct only. | [optional] 
**price_model_percentage** | [**PriceModelPercentage**](PriceModelPercentage.md) | The configuration for the Percentage pricing model. Applicable to Direct only. | [optional] 
**price_model_tiered** | [**PriceModelTiered**](PriceModelTiered.md) | The configuration for the Tiered pricing model. Applicable to Direct only. | [optional] 
**price_model_tiered_percentage** | [**PriceModelTieredPercentage**](PriceModelTieredPercentage.md) | The configuration for the Tiered Percentage pricing model. Applicable to Direct only. | [optional] 
**price_model_volume** | [**PriceModelVolume**](PriceModelVolume.md) | The configuration for the Bulk pricing model. Applicable to Direct only. | [optional] 
**time_unit** | [**TimeUnit**](TimeUnit.md) | The term unit for the commit amount. Applicable to Direct only. | [optional] 

## Example

```python
from suger_sdk_python.models.billable_dimension import BillableDimension

# TODO update the JSON string below
json = "{}"
# create an instance of BillableDimension from a JSON string
billable_dimension_instance = BillableDimension.from_json(json)
# print the JSON string representation of the object
print(BillableDimension.to_json())

# convert the object into a dict
billable_dimension_dict = billable_dimension_instance.to_dict()
# create an instance of BillableDimension from a dict
billable_dimension_from_dict = BillableDimension.from_dict(billable_dimension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


