# CreateIntegrationParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** |  | [optional] 
**info** | [**IntegrationInfo**](IntegrationInfo.md) |  | 
**organization_id** | **str** |  | 
**partner** | [**Partner**](Partner.md) |  | 
**service** | [**PartnerService**](PartnerService.md) |  | 

## Example

```python
from openapi_client.models.create_integration_params import CreateIntegrationParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateIntegrationParams from a JSON string
create_integration_params_instance = CreateIntegrationParams.from_json(json)
# print the JSON string representation of the object
print CreateIntegrationParams.to_json()

# convert the object into a dict
create_integration_params_dict = create_integration_params_instance.to_dict()
# create an instance of CreateIntegrationParams from a dict
create_integration_params_form_dict = create_integration_params.from_dict(create_integration_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


