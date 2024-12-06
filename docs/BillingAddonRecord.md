# BillingAddonRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | [optional] 
**charge_on** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from suger_sdk_python.models.billing_addon_record import BillingAddonRecord

# TODO update the JSON string below
json = "{}"
# create an instance of BillingAddonRecord from a JSON string
billing_addon_record_instance = BillingAddonRecord.from_json(json)
# print the JSON string representation of the object
print(BillingAddonRecord.to_json())

# convert the object into a dict
billing_addon_record_dict = billing_addon_record_instance.to_dict()
# create an instance of BillingAddonRecord from a dict
billing_addon_record_from_dict = BillingAddonRecord.from_dict(billing_addon_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


