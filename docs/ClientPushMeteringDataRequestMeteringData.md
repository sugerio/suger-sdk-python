# ClientPushMeteringDataRequestMeteringData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time** | **int** | example:  1666854480406 | [optional] 
**instance_id** | **str** | example:  gtm-cn-20p314k5h05 | [optional] 
**metering_assist** | **str** | example:  test001 | [optional] 
**metering_entity** | **str** | example:  {\&quot;VirtualCpu\&quot;:10} | [optional] 
**start_time** | **int** | example:  1662284820000 | [optional] 

## Example

```python
from suger_sdk_python.models.client_push_metering_data_request_metering_data import ClientPushMeteringDataRequestMeteringData

# TODO update the JSON string below
json = "{}"
# create an instance of ClientPushMeteringDataRequestMeteringData from a JSON string
client_push_metering_data_request_metering_data_instance = ClientPushMeteringDataRequestMeteringData.from_json(json)
# print the JSON string representation of the object
print(ClientPushMeteringDataRequestMeteringData.to_json())

# convert the object into a dict
client_push_metering_data_request_metering_data_dict = client_push_metering_data_request_metering_data_instance.to_dict()
# create an instance of ClientPushMeteringDataRequestMeteringData from a dict
client_push_metering_data_request_metering_data_from_dict = ClientPushMeteringDataRequestMeteringData.from_dict(client_push_metering_data_request_metering_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


