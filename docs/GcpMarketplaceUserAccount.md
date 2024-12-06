# GcpMarketplaceUserAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approvals** | [**List[GcpMarketplaceUserAccountApproval]**](GcpMarketplaceUserAccountApproval.md) | The approvals for this account, that are permitted or have been completed. | [optional] 
**billing_account_id** | **str** | The buyer&#39;s GCP billing account ID. | [optional] 
**create_time** | **datetime** | RFC3339 UTC timestamp | [optional] 
**id** | **str** | GCP Marketplace User Account ID. | [optional] 
**input_properties** | **List[int]** |  | [optional] 
**name** | **str** | The resource name of the account. Account names have the form providers/{provider_id}/accounts/{account_id}. | [optional] 
**provider** | **str** | The identifier of the service provider (SaaS Seller) that this account was created against. | [optional] 
**state** | [**GcpMarketplaceUserAccountState**](GcpMarketplaceUserAccountState.md) | The state of the account. An account might not be able to make a purchase if the billing account is suspended. | [optional] 
**update_time** | **datetime** | RFC3339 UTC timestamp | [optional] 
**user_info** | [**GcpUserInfo**](GcpUserInfo.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.gcp_marketplace_user_account import GcpMarketplaceUserAccount

# TODO update the JSON string below
json = "{}"
# create an instance of GcpMarketplaceUserAccount from a JSON string
gcp_marketplace_user_account_instance = GcpMarketplaceUserAccount.from_json(json)
# print the JSON string representation of the object
print(GcpMarketplaceUserAccount.to_json())

# convert the object into a dict
gcp_marketplace_user_account_dict = gcp_marketplace_user_account_instance.to_dict()
# create an instance of GcpMarketplaceUserAccount from a dict
gcp_marketplace_user_account_from_dict = GcpMarketplaceUserAccount.from_dict(gcp_marketplace_user_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


