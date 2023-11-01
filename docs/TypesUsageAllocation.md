# TypesUsageAllocation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocated_usage_quantity** | **int** | The total quantity allocated to this bucket of usage.  This member is required. | [optional] 
**tags** | [**List[GithubComAwsAwsSdkGoV2ServiceMarketplacemeteringTypesTag]**](GithubComAwsAwsSdkGoV2ServiceMarketplacemeteringTypesTag.md) | The set of tags that define the bucket of usage. For the bucket of items with no tags, this parameter can be left out. | [optional] 

## Example

```python
from openapi_client.models.types_usage_allocation import TypesUsageAllocation

# TODO update the JSON string below
json = "{}"
# create an instance of TypesUsageAllocation from a JSON string
types_usage_allocation_instance = TypesUsageAllocation.from_json(json)
# print the JSON string representation of the object
print TypesUsageAllocation.to_json()

# convert the object into a dict
types_usage_allocation_dict = types_usage_allocation_instance.to_dict()
# create an instance of TypesUsageAllocation from a dict
types_usage_allocation_form_dict = types_usage_allocation.from_dict(types_usage_allocation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


