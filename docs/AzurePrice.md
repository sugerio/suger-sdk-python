# AzurePrice


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_code** | **str** | ISO currency code, Three characters | [optional] 
**open_price** | **float** |  | [optional] 
**price_tier_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.azure_price import AzurePrice

# TODO update the JSON string below
json = "{}"
# create an instance of AzurePrice from a JSON string
azure_price_instance = AzurePrice.from_json(json)
# print the JSON string representation of the object
print AzurePrice.to_json()

# convert the object into a dict
azure_price_dict = azure_price_instance.to_dict()
# create an instance of AzurePrice from a dict
azure_price_form_dict = azure_price.from_dict(azure_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


