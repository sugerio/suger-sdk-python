# ServicecontrolStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | Code: The status code, which should be an enum value of google.rpc.Code. | [optional] 
**details** | **List[List[int]]** | Details: A list of messages that carry the error details. There is a common set of message types for APIs to use. | [optional] 
**message** | **str** | Message: A developer-facing error message, which should be in English. Any user-facing error message should be localized and sent in the google.rpc.Status.details field, or localized by the client. | [optional] 

## Example

```python
from suger_sdk_python.models.servicecontrol_status import ServicecontrolStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ServicecontrolStatus from a JSON string
servicecontrol_status_instance = ServicecontrolStatus.from_json(json)
# print the JSON string representation of the object
print(ServicecontrolStatus.to_json())

# convert the object into a dict
servicecontrol_status_dict = servicecontrol_status_instance.to_dict()
# create an instance of ServicecontrolStatus from a dict
servicecontrol_status_from_dict = ServicecontrolStatus.from_dict(servicecontrol_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


