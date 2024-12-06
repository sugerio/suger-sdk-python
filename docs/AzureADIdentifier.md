# AzureADIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_account_id** | **str** | Azure Billing Account ID | [optional] 
**customer_id** | **str** |  | [optional] 
**email_id** | **str** | Email address | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**license_type** | **str** | Azure License Type | [optional] 
**object_id** | **str** |  | [optional] 
**puid** | **str** | ID of the user, used as External ID of suger IdentityBuyer. | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.azure_ad_identifier import AzureADIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of AzureADIdentifier from a JSON string
azure_ad_identifier_instance = AzureADIdentifier.from_json(json)
# print the JSON string representation of the object
print(AzureADIdentifier.to_json())

# convert the object into a dict
azure_ad_identifier_dict = azure_ad_identifier_instance.to_dict()
# create an instance of AzureADIdentifier from a dict
azure_ad_identifier_from_dict = AzureADIdentifier.from_dict(azure_ad_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


