# GcpPeriodDuration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | such as 1, 6, 12 | [optional] 
**unit** | [**GcpPeriodDurationUnit**](GcpPeriodDurationUnit.md) |  | [optional] 

## Example

```python
from openapi_client.models.gcp_period_duration import GcpPeriodDuration

# TODO update the JSON string below
json = "{}"
# create an instance of GcpPeriodDuration from a JSON string
gcp_period_duration_instance = GcpPeriodDuration.from_json(json)
# print the JSON string representation of the object
print GcpPeriodDuration.to_json()

# convert the object into a dict
gcp_period_duration_dict = gcp_period_duration_instance.to_dict()
# create an instance of GcpPeriodDuration from a dict
gcp_period_duration_form_dict = gcp_period_duration.from_dict(gcp_period_duration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


