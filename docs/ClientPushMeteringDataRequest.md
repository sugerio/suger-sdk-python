# ClientPushMeteringDataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metering** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.client_push_metering_data_request import ClientPushMeteringDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClientPushMeteringDataRequest from a JSON string
client_push_metering_data_request_instance = ClientPushMeteringDataRequest.from_json(json)
# print the JSON string representation of the object
print(ClientPushMeteringDataRequest.to_json())

# convert the object into a dict
client_push_metering_data_request_dict = client_push_metering_data_request_instance.to_dict()
# create an instance of ClientPushMeteringDataRequest from a dict
client_push_metering_data_request_from_dict = ClientPushMeteringDataRequest.from_dict(client_push_metering_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


