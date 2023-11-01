# OrbExternalConnection


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_connection_name** | **str** |  | [optional] 
**external_entity_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.orb_external_connection import OrbExternalConnection

# TODO update the JSON string below
json = "{}"
# create an instance of OrbExternalConnection from a JSON string
orb_external_connection_instance = OrbExternalConnection.from_json(json)
# print the JSON string representation of the object
print OrbExternalConnection.to_json()

# convert the object into a dict
orb_external_connection_dict = orb_external_connection_instance.to_dict()
# create an instance of OrbExternalConnection from a dict
orb_external_connection_form_dict = orb_external_connection.from_dict(orb_external_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


