# GcpMarketplaceUserAccountApproval


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**reason** | **str** | An explanation for the state of the approval. | [optional] 
**state** | [**GcpMarketplaceUserAccountApprovalState**](GcpMarketplaceUserAccountApprovalState.md) |  | [optional] 
**update_time** | **str** | RFC3339 UTC timestamp | [optional] 

## Example

```python
from suger_sdk_python.models.gcp_marketplace_user_account_approval import GcpMarketplaceUserAccountApproval

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplaceUserAccountApproval from a JSON string
gcp_marketplace_user_account_approval_instance = GcpMarketplaceUserAccountApproval.from_json(json)
# print the JSON string representation of the object
print(GcpMarketplaceUserAccountApproval.to_json())

# convert the object into a dict
gcp_marketplace_user_account_approval_dict = gcp_marketplace_user_account_approval_instance.to_dict()
# create an instance of GcpMarketplaceUserAccountApproval from a dict
gcp_marketplace_user_account_approval_from_dict = GcpMarketplaceUserAccountApproval.from_dict(gcp_marketplace_user_account_approval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


