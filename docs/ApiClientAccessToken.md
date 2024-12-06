# ApiClientAccessToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | [optional] 
**expires_in** | **int** | The token expires in 1 hour | [optional] 
**expires_on** | **datetime** | The UTC timestamp when the token expires | [optional] 
**token_type** | **str** |  | [optional] [default to 'Bearer']

## Example

```python
from suger_sdk_python.models.api_client_access_token import ApiClientAccessToken

# TODO update the JSON string below
json = "{}"
# create an instance of ApiClientAccessToken from a JSON string
api_client_access_token_instance = ApiClientAccessToken.from_json(json)
# print the JSON string representation of the object
print(ApiClientAccessToken.to_json())

# convert the object into a dict
api_client_access_token_dict = api_client_access_token_instance.to_dict()
# create an instance of ApiClientAccessToken from a dict
api_client_access_token_from_dict = ApiClientAccessToken.from_dict(api_client_access_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


