# ServicecontrolReportError


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation_id** | **str** | OperationId: The Operation.operation_id value from the request. | [optional] 
**status** | [**ServicecontrolStatus**](ServicecontrolStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.servicecontrol_report_error import ServicecontrolReportError

# TODO update the JSON string below
json = "{}"
# create an instance of ServicecontrolReportError from a JSON string
servicecontrol_report_error_instance = ServicecontrolReportError.from_json(json)
# print the JSON string representation of the object
print ServicecontrolReportError.to_json()

# convert the object into a dict
servicecontrol_report_error_dict = servicecontrol_report_error_instance.to_dict()
# create an instance of ServicecontrolReportError from a dict
servicecontrol_report_error_form_dict = servicecontrol_report_error.from_dict(servicecontrol_report_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


