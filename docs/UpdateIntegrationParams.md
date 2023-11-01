# UpdateIntegrationParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | [**IntegrationInfo**](IntegrationInfo.md) |  | 
**organization_id** | **str** |  | 
**partner** | [**Partner**](Partner.md) |  | 
**service** | [**PartnerService**](PartnerService.md) |  | 

## Example

```python
from openapi_client.models.update_integration_params import UpdateIntegrationParams

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateIntegrationParams from a JSON string
update_integration_params_instance = UpdateIntegrationParams.from_json(json)
# print the JSON string representation of the object
print UpdateIntegrationParams.to_json()

# convert the object into a dict
update_integration_params_dict = update_integration_params_instance.to_dict()
# create an instance of UpdateIntegrationParams from a dict
update_integration_params_form_dict = update_integration_params.from_dict(update_integration_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


