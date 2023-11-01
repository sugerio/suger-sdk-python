# OrbItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**external_connections** | [**List[OrbExternalConnection]**](OrbExternalConnection.md) |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.orb_item import OrbItem

# TODO update the JSON string below
json = "{}"
# create an instance of OrbItem from a JSON string
orb_item_instance = OrbItem.from_json(json)
# print the JSON string representation of the object
print OrbItem.to_json()

# convert the object into a dict
orb_item_dict = orb_item_instance.to_dict()
# create an instance of OrbItem from a dict
orb_item_form_dict = orb_item.from_dict(orb_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


