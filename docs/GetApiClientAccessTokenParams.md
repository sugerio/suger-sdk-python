# GetApiClientAccessTokenParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the API Client. | 
**organization_id** | **str** |  | 
**secret** | **str** | The secret of the API Client. | 

## Example

```python
from suger_sdk_python.models.get_api_client_access_token_params import GetApiClientAccessTokenParams

# TODO update the JSON string below
json = "{}"
# create an instance of GetApiClientAccessTokenParams from a JSON string
get_api_client_access_token_params_instance = GetApiClientAccessTokenParams.from_json(json)
# print the JSON string representation of the object
print(GetApiClientAccessTokenParams.to_json())

# convert the object into a dict
get_api_client_access_token_params_dict = get_api_client_access_token_params_instance.to_dict()
# create an instance of GetApiClientAccessTokenParams from a dict
get_api_client_access_token_params_from_dict = GetApiClientAccessTokenParams.from_dict(get_api_client_access_token_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


