# ListUsageMeteringDailyVerificationsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_offset** | **int** |  | [optional] 
**usage_metering_daily_verifications** | [**List[UsageMeteringDailyVerification]**](UsageMeteringDailyVerification.md) | per day per dimension. | [optional] 

## Example

```python
from openapi_client.models.list_usage_metering_daily_verifications_response import ListUsageMeteringDailyVerificationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListUsageMeteringDailyVerificationsResponse from a JSON string
list_usage_metering_daily_verifications_response_instance = ListUsageMeteringDailyVerificationsResponse.from_json(json)
# print the JSON string representation of the object
print ListUsageMeteringDailyVerificationsResponse.to_json()

# convert the object into a dict
list_usage_metering_daily_verifications_response_dict = list_usage_metering_daily_verifications_response_instance.to_dict()
# create an instance of ListUsageMeteringDailyVerificationsResponse from a dict
list_usage_metering_daily_verifications_response_form_dict = list_usage_metering_daily_verifications_response.from_dict(list_usage_metering_daily_verifications_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


