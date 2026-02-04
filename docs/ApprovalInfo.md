# ApprovalInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approval_status** | [**ApprovalStatus**](ApprovalStatus.md) | ApprovalStatus holds the current approval status of the offer | \&quot;Submitted\&quot; | \&quot;Approved\&quot; | \&quot;Declined\&quot; | \&quot;Action Required\&quot;; | [optional] 
**decision_date** | **str** | DecisionDate is when the final approval/decline happened (nil when pending) Latest DecisionDate | [optional] 
**message** | **str** | Message is the reason or explanation provided when the approval status is set to Declined or Action Required. It always stores the latest message for the current status transition. Historical messages are stored in notification events. | [optional] 
**request_date** | **str** | Latest  RequestDate | [optional] 

## Example

```python
from suger_sdk_python.models.approval_info import ApprovalInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovalInfo from a JSON string
approval_info_instance = ApprovalInfo.from_json(json)
# print the JSON string representation of the object
print(ApprovalInfo.to_json())

# convert the object into a dict
approval_info_dict = approval_info_instance.to_dict()
# create an instance of ApprovalInfo from a dict
approval_info_from_dict = ApprovalInfo.from_dict(approval_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


