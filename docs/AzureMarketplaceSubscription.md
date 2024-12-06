# AzureMarketplaceSubscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_customer_operations** | **List[str]** |  | [optional] 
**auto_renew** | **bool** |  | [optional] 
**beneficiary** | [**AzureADIdentifier**](AzureADIdentifier.md) |  | [optional] 
**created** | **datetime** |  | [optional] 
**fulfillment_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**is_free_trial** | **bool** |  | [optional] 
**is_test** | **bool** |  | [optional] 
**last_modified** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**offer_id** | **str** |  | [optional] 
**plan_id** | **str** |  | [optional] 
**publisher_id** | **str** |  | [optional] 
**purchaser** | [**AzureADIdentifier**](AzureADIdentifier.md) |  | [optional] 
**quantity** | **int** |  | [optional] 
**saas_subscription_status** | [**AzureMarketplaceSubscriptionStatus**](AzureMarketplaceSubscriptionStatus.md) |  | [optional] 
**sandbox_type** | **str** |  | [optional] 
**session_id** | **str** |  | [optional] 
**session_mode** | **str** |  | [optional] 
**store_front** | **str** |  | [optional] 
**term** | [**AzureTerm**](AzureTerm.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_marketplace_subscription import AzureMarketplaceSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of AzureMarketplaceSubscription from a JSON string
azure_marketplace_subscription_instance = AzureMarketplaceSubscription.from_json(json)
# print the JSON string representation of the object
print(AzureMarketplaceSubscription.to_json())

# convert the object into a dict
azure_marketplace_subscription_dict = azure_marketplace_subscription_instance.to_dict()
# create an instance of AzureMarketplaceSubscription from a dict
azure_marketplace_subscription_from_dict = AzureMarketplaceSubscription.from_dict(azure_marketplace_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


