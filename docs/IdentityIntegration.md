# IdentityIntegration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** |  | [optional] 
**creation_time** | **datetime** |  | [optional] 
**info** | [**IntegrationInfo**](IntegrationInfo.md) |  | [optional] 
**last_update_time** | **datetime** |  | [optional] 
**last_updated_by** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**partner** | **str** |  | [optional] 
**service** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.identity_integration import IdentityIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of IdentityIntegration from a JSON string
identity_integration_instance = IdentityIntegration.from_json(json)
# print the JSON string representation of the object
print IdentityIntegration.to_json()

# convert the object into a dict
identity_integration_dict = identity_integration_instance.to_dict()
# create an instance of IdentityIntegration from a dict
identity_integration_form_dict = identity_integration.from_dict(identity_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


