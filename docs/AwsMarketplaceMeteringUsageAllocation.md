# AwsMarketplaceMeteringUsageAllocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocated_usage_quantity** | **int** | The total quantity allocated to this bucket of usage. | [optional] 
**tags** | [**List[AwsMarketplaceMeteringTag]**](AwsMarketplaceMeteringTag.md) | The set of tags that define the bucket of usage. For the bucket of items with no tags, this parameter can be left out. | [optional] 

## Example

```python
from suger_sdk_python.models.aws_marketplace_metering_usage_allocation import AwsMarketplaceMeteringUsageAllocation

# TODO update the JSON string below
json = "{}"
# create an instance of AwsMarketplaceMeteringUsageAllocation from a JSON string
aws_marketplace_metering_usage_allocation_instance = AwsMarketplaceMeteringUsageAllocation.from_json(json)
# print the JSON string representation of the object
print(AwsMarketplaceMeteringUsageAllocation.to_json())

# convert the object into a dict
aws_marketplace_metering_usage_allocation_dict = aws_marketplace_metering_usage_allocation_instance.to_dict()
# create an instance of AwsMarketplaceMeteringUsageAllocation from a dict
aws_marketplace_metering_usage_allocation_from_dict = AwsMarketplaceMeteringUsageAllocation.from_dict(aws_marketplace_metering_usage_allocation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


