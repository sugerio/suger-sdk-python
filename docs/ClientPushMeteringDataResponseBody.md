# ClientPushMeteringDataResponseBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** |  | [optional] 
**success** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.client_push_metering_data_response_body import ClientPushMeteringDataResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of ClientPushMeteringDataResponseBody from a JSON string
client_push_metering_data_response_body_instance = ClientPushMeteringDataResponseBody.from_json(json)
# print the JSON string representation of the object
print ClientPushMeteringDataResponseBody.to_json()

# convert the object into a dict
client_push_metering_data_response_body_dict = client_push_metering_data_response_body_instance.to_dict()
# create an instance of ClientPushMeteringDataResponseBody from a dict
client_push_metering_data_response_body_form_dict = client_push_metering_data_response_body.from_dict(client_push_metering_data_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


