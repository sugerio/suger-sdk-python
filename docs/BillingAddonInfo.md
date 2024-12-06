# BillingAddonInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 

## Example

```python
from suger_sdk_python.models.billing_addon_info import BillingAddonInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BillingAddonInfo from a JSON string
billing_addon_info_instance = BillingAddonInfo.from_json(json)
# print the JSON string representation of the object
print(BillingAddonInfo.to_json())

# convert the object into a dict
billing_addon_info_dict = billing_addon_info_instance.to_dict()
# create an instance of BillingAddonInfo from a dict
billing_addon_info_from_dict = BillingAddonInfo.from_dict(billing_addon_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


