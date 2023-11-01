# ServicecontrolReportResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_errors** | [**List[ServicecontrolReportError]**](ServicecontrolReportError.md) | ReportErrors: Partial failures, one for each &#x60;Operation&#x60; in the request that failed processing. There are three possible combinations of the RPC status: 1. The combination of a successful RPC status and an empty &#x60;report_errors&#x60; list indicates a complete success where all &#x60;Operations&#x60; in the request are processed successfully. 2. The combination of a successful RPC status and a non-empty &#x60;report_errors&#x60; list indicates a partial success where some &#x60;Operations&#x60; in the request succeeded. Each &#x60;Operation&#x60; that failed processing has a corresponding item in this list. 3. A failed RPC status indicates a general non-deterministic failure. When this happens, it&#39;s impossible to know which of the &#39;Operations&#39; in the request succeeded or failed. | [optional] 
**service_config_id** | **str** | ServiceConfigId: The actual config id used to process the request. | [optional] 
**service_rollout_id** | **str** | ServiceRolloutId: The current service rollout id used to process the request. | [optional] 

## Example

```python
from openapi_client.models.servicecontrol_report_response import ServicecontrolReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServicecontrolReportResponse from a JSON string
servicecontrol_report_response_instance = ServicecontrolReportResponse.from_json(json)
# print the JSON string representation of the object
print ServicecontrolReportResponse.to_json()

# convert the object into a dict
servicecontrol_report_response_dict = servicecontrol_report_response_instance.to_dict()
# create an instance of ServicecontrolReportResponse from a dict
servicecontrol_report_response_form_dict = servicecontrol_report_response.from_dict(servicecontrol_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


