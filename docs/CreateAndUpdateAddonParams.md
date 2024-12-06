# CreateAndUpdateAddonParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The amount of the addon. | [optional] 
**description** | **str** | The description of the addon. | [optional] 
**name** | **str** | The name of the addon. | [optional] 

## Example

```python
from suger_sdk_python.models.create_and_update_addon_params import CreateAndUpdateAddonParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAndUpdateAddonParams from a JSON string
create_and_update_addon_params_instance = CreateAndUpdateAddonParams.from_json(json)
# print the JSON string representation of the object
print(CreateAndUpdateAddonParams.to_json())

# convert the object into a dict
create_and_update_addon_params_dict = create_and_update_addon_params_instance.to_dict()
# create an instance of CreateAndUpdateAddonParams from a dict
create_and_update_addon_params_from_dict = CreateAndUpdateAddonParams.from_dict(create_and_update_addon_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


