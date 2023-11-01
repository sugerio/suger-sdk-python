# UsageCount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credit_count** | **float** | The count of this dimension usage records that are handled as credit. | [optional] 
**included_count** | **float** | The count of this dimension usage records that are handled as included in IncludedBaseQuantity | [optional] 
**reported_count** | **float** | The count of this dimension usage records that are reported to cloud vendors. | [optional] 

## Example

```python
from openapi_client.models.usage_count import UsageCount

# TODO update the JSON string below
json = "{}"
# create an instance of UsageCount from a JSON string
usage_count_instance = UsageCount.from_json(json)
# print the JSON string representation of the object
print UsageCount.to_json()

# convert the object into a dict
usage_count_dict = usage_count_instance.to_dict()
# create an instance of UsageCount from a dict
usage_count_form_dict = usage_count.from_dict(usage_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


