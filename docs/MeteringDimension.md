# MeteringDimension

The dimension to meter usage in entitlement.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**included_base_quantities** | [**List[AzureIncludedBaseQuantity]**](AzureIncludedBaseQuantity.md) | how many quantities of this dimension are included in the commit. | [optional] 
**key** | **str** |  | [optional] 
**name** | **str** | Display name of the dimension. For GCP Marketplace, it is the metering metric ID without plan prefix. | [optional] 
**plan_id** | **str** | The plan ID of the metering dimension. Applicable to GCP Marketplace only. No ISO duration suffix. | [optional] 
**plan_name** | **str** | The name of the plan for the metering dimension. Applicable to GCP Marketplace only. It may contains the ISO duration suffix, such as P1Y. | [optional] 
**price_tiers** | [**List[GcpPriceTier]**](GcpPriceTier.md) | The price tiers of the metering dimension. Applicable to GCP Marketplace only. | [optional] 
**rate** | **float** | The unit price of this usage metering dimension. | [optional] 
**sku_id** | **str** | The SKU ID of the metering dimension. Applicable to GCP Marketplace only. | [optional] 
**types** | **List[str]** |  | [optional] 
**usage_count** | [**UsageCount**](UsageCount.md) |  | [optional] 
**value_type** | [**ValueType**](ValueType.md) |  | [optional] 

## Example

```python
from openapi_client.models.metering_dimension import MeteringDimension

# TODO update the JSON string below
json = "{}"
# create an instance of MeteringDimension from a JSON string
metering_dimension_instance = MeteringDimension.from_json(json)
# print the JSON string representation of the object
print MeteringDimension.to_json()

# convert the object into a dict
metering_dimension_dict = metering_dimension_instance.to_dict()
# create an instance of MeteringDimension from a dict
metering_dimension_form_dict = metering_dimension.from_dict(metering_dimension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


