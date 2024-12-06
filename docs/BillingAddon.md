# BillingAddon


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_time** | **datetime** |  | [optional] 
**description** | **str** | Description of the addon | [optional] 
**id** | **str** |  | [optional] 
**info** | [**BillingAddonInfo**](BillingAddonInfo.md) |  | [optional] 
**last_update_time** | **datetime** |  | [optional] 
**name** | **str** | Name of the addon, e.g. \&quot;Support Plan\&quot; | [optional] 
**organization_id** | **str** |  | [optional] 
**status** | [**BillingAddonStatus**](BillingAddonStatus.md) |  | [optional] 

## Example

```python
from suger_sdk_python.models.billing_addon import BillingAddon

# TODO update the JSON string below
json = "{}"
# create an instance of BillingAddon from a JSON string
billing_addon_instance = BillingAddon.from_json(json)
# print the JSON string representation of the object
print(BillingAddon.to_json())

# convert the object into a dict
billing_addon_dict = billing_addon_instance.to_dict()
# create an instance of BillingAddon from a dict
billing_addon_from_dict = BillingAddon.from_dict(billing_addon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


